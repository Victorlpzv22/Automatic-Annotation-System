import modules.Verbs as verb
import modules.Noun as Noun
'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This module extracts the nouns per verbs
'''

def nounperverb(oracion):
    try:
        nounverb = Noun.nouns(oracion)/verb.count_verbs(oracion)
    except:
        nounverb = 0
    return nounverb
    
    