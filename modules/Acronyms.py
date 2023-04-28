'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This module extracts the acronyms of a asentence
'''

def count_acronyms(sentence):
    sentence=sentence.replace("WI FI", 'WIFI')
    blacklist=['XX', 'XXL', 'XL', 'OK', 'USA', 'UPM', 'UK'] #unconsidered acronyms
    words = sentence.split()
    acrs = []
    for word in words:
        word = word.replace(",", " ").replace(".", " ").replace("?", " ").replace(";", " ").replace(":", " ").replace("!", " ").strip()
        if word.isupper() and len(word) > 1 and word not in blacklist and word not in acrs:
            acrs.append(word)
    return (len(acrs))
