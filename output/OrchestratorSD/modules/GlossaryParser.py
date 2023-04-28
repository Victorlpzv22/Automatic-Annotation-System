import os
import re

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This module converts the glossary txt into a python variable
'''

absRoute = f"{os.getcwd()}\\glossary\\technicalWords.txt"

def run():
    with open(absRoute, "r") as inputFile:
        strings = inputFile.read().split("\n")

    stringList = []
    for s in strings:
        matches = re.findall(r'\((.*?)\)', s)
        for match in matches:
            s = s.replace(f"({match})", "").strip()
            if match and (match not in stringList):
                stringList.append(match.strip())
        if s and (s not in stringList):
            stringList.append(s.strip())
    return stringList

def add(term):
    with open(absRoute, "a") as txt:
        txt.write("\n"+term)
        txt.close
