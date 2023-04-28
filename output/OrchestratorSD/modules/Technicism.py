import modules.GlossaryParser as glo

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This modules extracts the technicism of a sentence
'''

def technicism(text, glossary):
    try:
        text = " " + text.replace(",", " ").replace(".", " ").replace("?", " ").replace(";", " ").replace(":", " ").replace("!", " ") + " "
        palabras_encontradas = []
        for palabra in glossary:
            texto2 = text
            if not palabra.isupper():
                texto2 = text.lower()
                palabra = palabra.lower()

            palabrasExtendidas = [f" {palabra} ", f" {palabra}s ", f" {palabra}es ", f" {palabra}ing "]
            for palabraExtendida in palabrasExtendidas:
                if palabraExtendida in texto2: 
                    palabras_encontradas.append(palabraExtendida.strip())
                    break
                        
        tecnicismos = filter_substrings(palabras_encontradas)
        
        for palabra in tecnicismos:
            if palabra.lower() not in text.lower(): tecnicismos.remove(palabra) 
        return (len(tecnicismos), tecnicismos) 
        
    except:
        return (0, 0)

def filter_substrings(strings):
    strings = list(set(strings))
    result = []
    for string in strings:
        if not any([string in s for s in strings if string != s]):
            result.append(string)
    return result

    
 
