import xml.etree.ElementTree as ET
import traceback
import Apps.Strings as strings
import Apps.Functions as fun
from datetime import datetime

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script shows the differences between two XML files according to the semantic density of their sentences
'''

def comparatorSD():
    map = {"sd++": 3, "sd+": 2,"sd-": 1,"sd--": 0}
    fun.clear()
    print(strings.welcome.get("ComparatorMenu"))
    exit = False
    while not exit:
        error = True
        print(strings.comparatorMenu)
         #Option 2 means exit
        if fun.inputOption(1, 2, strings.typeOption) == 2:  
            exit = True
            fun.clear()
            break

        fun.clear()
        print(strings.welcome.get("GlossaryMenu"))
        
        error = True
        fun.clear()
        print(strings.welcome.get("ComparatorMenu"))
        while error:
            try:
                input1 = fun.openFile("xml")
                tree1 = ET.parse(input1)
                error = False
            except:
                print(strings.errorInputFile)
                fun.showFiles("xml")
        
        error = True
        while error:
            try:
                input2 = fun.openFile("xml")
                tree2 = ET.parse(input2)
                error = False
            except:
                print(strings.errorInputFile)
                fun.showFiles("xml")
        
        print(strings.compareMode)
        mode = fun.inputOption(1, 2, strings.typeOption)
        
        writeMode = input(strings.writeMode) 
        if writeMode.lower() == "y": write_option = True # write in a txt log file
        else: write_option = False #write in the console
        
        try:
            (list_sen, list1_sd, list2_sd) = extractElements (tree1.getroot(), tree2.getroot())    
            if len(list1_sd) == len(list2_sd): #check if two files have the same numbre of sentences
                (oraciones, errorTotal, numbers1, numbers2) = compare(mode, map, list_sen, list1_sd, list2_sd, write_option)
                if write_option == False: result(oraciones, errorTotal, numbers1, numbers2) 
            else: print(strings.errorLength)
        except:
            print(strings.errorCompare)
            traceback.print_exc()

        fun.pressEnter()
        fun.clear()
        
#extract the content of segment and semantic density in both files
def extractElements(root1, root2) -> tuple:
    list1_sd = []
    list2_sd = []
    list_sen = []
    
    for segment in root1.iter('segment'): list_sen.append(segment.text)
    for segment in root1.findall('.//segment'): list1_sd.append(segment.get('features').replace("semantic-density;", ""))
    for segment in root2.findall('.//segment'): list2_sd.append(segment.get('features').replace("semantic-density;", ""))

    return(list_sen, list1_sd, list2_sd)

#shows the comparation of all categories   
def compare(mode, map, list_sen, list1_sd, list2_sd, write_option):

    #category counters
    numbers1 = [0, 0, 0, 0]
    numbers2 = [0, 0, 0, 0]
    totalError = 0
    
    if write_option:
        now = datetime.now()
        w = open("./logs/log_"+now.strftime("%d-%m-%Y_%Hh%M'%S''")+".txt", 'w', encoding='utf-8')
        w.write(strings.files + "\n")
        
    else: print(strings.files)
    
    counter = 0
    
    for element in list1_sd: #compute the counters of each category
        totalError = totalError + abs(map[element]-map[list2_sd[counter]])
        if element == "sd--": numbers1[0] += 1
        elif element == "sd-": numbers1[1] += 1
        elif element == "sd+": numbers1[2] += 1
        else: numbers1[3] += 1
        
        if list2_sd[counter] == 'sd--': numbers2[0] += 1
        elif list2_sd[counter] == 'sd-': numbers2[1] += 1
        elif list2_sd[counter] == 'sd+': numbers2[2] += 1
        else: numbers2[3] += 1
        
        if mode == 1: #all sentences
            if element != list2_sd[counter]:
                spaces = 10-len(element)
                spaces2 = 10-len(list2_sd[counter])
                blanco = " "
                if write_option : w.write(element + blanco*spaces + list2_sd[counter] + blanco*spaces2 + list_sen[counter] + "\n")
                else:print(element + blanco*spaces + list2_sd[counter] + blanco*spaces2 + list_sen[counter])
                
            counter+=1 
        else: #diferrent sentences
            spaces=10-len(element)
            spaces2=10-len(list2_sd[counter])
            blanco=" "
            if write_option : w.write(element + blanco*spaces + list2_sd[counter] + blanco*spaces2 + list_sen[counter] + "\n")
            else: print(element + blanco*spaces + list2_sd[counter] + blanco*spaces2 + list_sen[counter])
                 
            counter+=1 
            
    if write_option :
        
        sentences=counter
        maxError=3*sentences
        score=totalError/maxError
        score=100*(1-score)
        w.write(f"\nThe total error is: {totalError} \nThe number of sentences is: {sentences}" + "\n") 
        w.write(f"The score of the comparison is: {score}%" + "\n")
        w.write(f"- SD++  File 1: {numbers1[3]}, File 2: {numbers2[3]}" + "\n")
        w.write(f"- SD+   File 1: {numbers1[2]}, File 2: {numbers2[2]}" + "\n")
        w.write(f"- SD-   File 1: {numbers1[1]}, File 2: {numbers2[1]}" + "\n")
        w.write(f"- SD--  File 1: {numbers1[0]}, File 2: {numbers2[0]}" + "\n")        
        
    return (counter, totalError, numbers1, numbers2)

#compute and calculate the score of the comparation   
def result(sentences, totalError, numbers1, numbers2):
    
    maxError=3*sentences
    score=totalError/maxError
    score=100*(1-score)
    
    print(f"\nThe total error is: {totalError} \nThe number of sentences is: {sentences}") 
    print(f"The score of the comparison is: {score}%")
    print(f"- SD++  File 1: {numbers1[3]}, File 2: {numbers2[3]}")
    print(f"- SD+   File 1: {numbers1[2]}, File 2: {numbers2[2]}")
    print(f"- SD-   File 1: {numbers1[1]}, File 2: {numbers2[1]}")
    print(f"- SD--  File 1: {numbers1[0]}, File 2: {numbers2[0]}")
   

if __name__ == "__main__":
    comparatorSD()
    
