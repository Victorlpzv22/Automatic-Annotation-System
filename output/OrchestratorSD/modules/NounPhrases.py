import spacy

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This script extracts the noun phrases of a sentence
'''

nlp = spacy.load('en_core_web_sm')

def noun_phrases(sentence) -> tuple[int, float]:
    try:
        doc = nlp(sentence)
        lista_gn = []
        str = ""
        valido = False
        
        for token in doc:
            if token.pos_ in ["DET", "PRON", "PROPN", "NOUN", "ADJ", "ADP"]:
                if token.pos_ in ["PRON", "PROPN", "NOUN", "ADJ"]:
                    valido = True
                str += " " + token.text
            elif token.text == ",":
                pass
            elif str != "" :
                if valido:
                    valido = False
                    lista_gn.append(str.strip())
                str = ""
        if str != "" :
            if valido:
                valido = False
                lista_gn.append(str.strip())
            str = ""

        cont = 0
        for gn in lista_gn:
            cont += gn.count(" ") + 1

        media = 0
        if len(lista_gn) != 0:
            media = cont/len(lista_gn)
            
        return media 
    except: return 0
    