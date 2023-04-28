import modules.NounPhrases as np
import modules.Technicism as tec
import modules.Acronyms as acr
import modules.Verbs as verb
import modules.NounPerVerb as npb
import modules.GlossaryParser as gp
import modules.ProgressBar as ProgressBar
import Strings as strings
import Functions as fun
import re


'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       22/04/23

ABOUT:      This script measures the parameters of a TXT file and gives the semantic densities
'''

def translatorSD():
    global glossary
    glossary = refreshGlossary()
    
    exit = False
    while not exit:
        fun.clear()
        print(strings.welcome.get("TranslatorMenu"))
        print(strings.translatorMenu)
        
        #Option 2 means exit
        if fun.inputOption(1, 2, strings.typeOption) == 2:  
            exit = True
            break
        
        fun.clear()
        print(strings.welcome.get("TranslatorMenu"))

        error = True
        while error:
            try:
                input1 = fun.openFile("txt")
                f = open(input1, 'r', encoding = 'utf-8')
                error = False
            except:
                print(strings.errorInputFile)
                fun.showFiles("txt")
        
        #repeat until the file doesnt exist or the user wants to overwrite it        
        repeate = True
        while repeate:        
            output = fun.openFile("xml", "output")
            repeate = False
            if fun.fileExisting(output): 
                repeate = True
                opcion = input(strings.fileExists)
                if opcion.upper() == "Y": repeate = False
            
        w = open(output, 'w', encoding = 'utf-8')
        
        #the user selects the mode to separate the sentences    
        print(strings.separationMode)
        lectureMode = fun.inputOption(1, 2, strings.typeOption)
        
        progressBar = ProgressBar.ProgressBar() #begining ProgressBar
        progressBar.start()
        
        (oraciones, categorias) = xmlContent(lectureMode, f.readlines())
        
        fun.writeXML(w, input1, oraciones, categorias)

        f.close()
        w.close()
        progressBar.stop() #ending ProgressBar
        fun.pressEnter()
        fun.clear()

def xmlContent(lectureMode, text) -> tuple: 
    id = 0 
    oraciones = {} 
    categorias = {} 

    for line in text:
        if lectureMode == 2:
            # Separate the content with the characters
            pattern = r'([?.!])'
            lines = re.split(pattern, line.strip())
            sentences = []
            for i in range(0, len(lines)-1, 2):
                sentences.append(lines[i] + lines[i+1]) 
        else: sentences = re.split('\n', line.strip())
        for sentence in sentences:
            if sentence != "":
                sentence.strip()
                oraciones[id] = sentence.replace("\n", "")
                categorias[id] = analyze(oraciones[id])
                id = id + 1
    return (oraciones, categorias)

#extract the parameter of a sentence   
def analyze(sentence) -> str:
    global glossary
    n_tec = tec.technicism(sentence, glossary)[0]
    d_tec = n_tec/len(sentence.split())
    n_acr = acr.count_acronyms(sentence)
    n_npb = npb.nounperverb(sentence)
    l_gn = np.noun_phrases(sentence)
    
    return semanticDensity(n_tec, d_tec, n_acr, n_npb, l_gn)

#give the semantic density category based on the parameters 
def semanticDensity(n_tec, d_tec, n_acr, n_npb, l_gn):
    if n_tec == 0 and n_npb <= 6 and n_acr == 0: return "sd--"
    elif n_acr >= 2 or n_tec >= 4  or d_tec >= 0.4: return "sd++"
    elif d_tec >= 0.26 or n_tec >= 2 or l_gn > 7: return "sd+"
    else: return "sd-"

#refresh the glossary
def refreshGlossary(): return gp.run()

if __name__ == "__main__":
    translatorSD()