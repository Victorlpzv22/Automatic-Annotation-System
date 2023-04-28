import spacy

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This script extracts the verbs of a sentence
'''

nlp = spacy.load('en_core_web_sm')

def count_verbs(sentence) -> int:
    try:
        doc = nlp(sentence)
        contador=0
        
        for token in doc:
            if token.pos_ in ["VERB"]:
                contador += 1
            elif token.pos_ in ["AUX"]:
                contador += 0.5
        return contador   
    except: return 0

