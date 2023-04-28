import os
import Strings as strings

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script stores the functions of the programm
'''

#Clear the terminal
def clear(): os.system("cls")

def pressEnter(): input("\nPress Enter to continue...")

#Loop until the user types a correct option
def inputOption(minValue, maxValue, inputString) -> int:
    repeateTypeOption = True
    while repeateTypeOption == True:
        try:
            option = int(input(inputString))
            if option >= minValue and option <= maxValue: repeateTypeOption = False
        except: continue
    return option

#Return the name of the specified file
def openFile(type, inout = "input") -> str: 
    if type == "xml": 
        if inout == "input": return "./xml/" + str(input(strings.xmlInputFile)) + ".xml"
        else: return "./xml/" + str(input(strings.xmlOutputFile)) + ".xml"
    elif type == "txt": 
        if inout == "input": return "./txt/" + str(input(strings.txtInputFile)) + ".txt"
        else: return "./txt/" + str(input(strings.txtOutputFile)) + ".txt"

#Returns True/False if the file exists in the directory
def fileExisting(file) -> bool: return os.path.isfile(os.getcwd() + file)

#Prints the current files that exists in the directory
def showFiles(path):
    print("The current files in the /" + path + " directory are:")
    for file in os.listdir(os.getcwd() + "/" + path): print(f"- {file}")
    print("\n")

#Round decimal numbers
def roundNum(num): return round(num, 3)

def writeXML(w, entrada, oraciones, categorias):
    w.write(strings.head_xml.replace("TITLE", entrada) + strings.body_xml_o)
    for id in oraciones.keys(): w.write(strings.segmento_xml.replace("ID", str(id)).replace("SD", str(categorias[id])).replace("CONTENT", oraciones[id]))
    w.write(strings.body_xml_c + strings.document_xml)