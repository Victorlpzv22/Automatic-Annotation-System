import xml.etree.ElementTree as ET
import traceback
import Apps.Strings as strings
import Apps.Functions as fun

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script extracts the content in "segment" labels in a XML file into a TXT file
'''

def parserSD():
    fun.clear()
    exit = False
    while not exit:
        print(strings.welcome.get("ParserMenu"))
        print(strings.parserMenu)

        #Option 2 means exit
        if fun.inputOption(1, 2, strings.typeOption) == 2:  
            exit = True
            fun.clear()
            break

        fun.clear()
        print(strings.welcome.get("ParserMenu"))

        #Repeat until the  XML file is correct
        repeat = True
        while repeat:
            try:
                inputFile = fun.openFile("xml")
                tree = ET.parse(inputFile)
                repeat = False
            except:
                print(strings.errorInputFile)
                fun.showFiles("xml")
                
        #Repeat until the user overwrites the file or the file doesnt exist       
        repeat = True
        while repeat:        
            output = fun.openFile("txt", "output")
            repeat = False
            if fun.fileExisting(output): 
                repeat = True
                option = str(input(strings.fileExists))
                if option.upper() == "Y": repeat = False #the file is overwrite
        
        try:
            w = open(output, 'w', encoding='utf-8')
            root = tree.getroot()

            #extract the content of the "segment" label
            for segment in root.iter('segment'):
                sentence = segment.text
                if sentence[-1] != "." and sentence[-1] != "?" and sentence[-1] != "!":
                    sentence += "."
                w.write(sentence + "\n")
                
            w.close()
        except:
            print(strings.errorParsing)
            traceback.print_exc()

        print('\nDone! 👍')
        fun.pressEnter()
        fun.clear()

if __name__ == "__main__":
    parserSD()