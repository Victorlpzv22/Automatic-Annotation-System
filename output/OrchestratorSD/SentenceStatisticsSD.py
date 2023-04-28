import modules.NounPhrases as np
import modules.Technicism as tec
import modules.Acronyms as acr
import modules.NounPerVerb as npv
import modules.GlossaryParser as gp
import modules.NounPerVerb as npv
import TranslatorSD as tra
import Strings as strings
import Functions as fun

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script takes a sentence and shows the users the statistics measured
'''

def sentenceStatisticsSD():
    glossary = refreshGlossary()
    exit = False
    while not exit:
        fun.clear()
        print(strings.welcome.get("SentenceMenu"))
        print(strings.sentenceMenu)
        
        #Option 2 means exit
        if fun.inputOption(1, 2, strings.typeOption) == 2:  
            exit = True
            fun.clear()
            break
        
        fun.clear()
        print(strings.welcome.get("SentenceMenu"))

        #repeat until the user writes a sentence
        sentence = ""
        while len(sentence) == 0:
            sentence = str(input(strings.typeSentence)).strip()
        
        (n_tec, tecns, d_tec, n_acr, n_npv, l_gn) = analyze(sentence, glossary)
        
        print(f"\nSemantic Density: {tra.semanticDensity(n_tec, d_tec, n_acr, n_npv, l_gn).upper()}\nNº of Technicisms: {n_tec}\nTechnicisms: {tecns}\nNº of Technicism per word: {fun.roundNum(d_tec)}\nNº of Acronyms: {fun.roundNum(n_acr)}\nNº of Noun per verbs: {fun.roundNum(n_npv)}\nAverage length of nominal groups: {fun.roundNum(l_gn)}")
        fun.pressEnter()
        fun.clear()
        
#this fuction extracts the parameters of a sentence
def analyze(sentence, glossary):
        (n_tec, tecns) = tec.technicism(sentence, glossary)
        d_tec = n_tec/len(sentence.split())
        n_acr = acr.count_acronyms(sentence)
        n_npv = npv.nounperverb(sentence)
        l_gn = np.noun_phrases(sentence)
        return (n_tec, tecns, d_tec, n_acr, n_npv, l_gn)
    
#refresh the glossary
def refreshGlossary(): return gp.run()

if __name__ == "__main__":
    sentenceStatisticsSD()