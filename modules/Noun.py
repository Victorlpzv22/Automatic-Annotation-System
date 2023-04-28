import spacy

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This module extracts the nouns of a sentence
'''

nlp = spacy.load('en_core_web_sm')

def nouns(sentence) -> int:
    try:
        doc = nlp(sentence)
        contador=0
        for token in doc:
            if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                contador += 1
        return contador   
    except: return 0