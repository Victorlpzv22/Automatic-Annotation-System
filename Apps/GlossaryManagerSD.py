import modules.GlossaryParser as gp
import Apps.Strings as strings
import Apps.Functions as fun

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script allows the user to check or add terms in the glossary
'''

def glossaryManagerSD(): 
    fun.clear()
    print(strings.welcome.get("GlossaryMenu"))
    exit = False
    while exit == False:
        print(strings.glossayMenu)
        
        #Option 2 means exit
        if fun.inputOption(1, 2, strings.typeOption) == 2:  
            exit = True
            fun.clear()
            break

        fun.clear()
        print(strings.welcome.get("GlossaryMenu"))

        #repeat until the user writes a term
        term = ""
        while len(term) == 0: term = str(input(strings.typeTerm)).strip()
        
        glossary = refreshGlossary()
        found = False
        #check if the term or a variable is in the glossary
        for termino in glossary: 
            if not term.isupper(): term = term.lower()
            if not termino.isupper(): termino = termino.lower()
            if term in [termino, termino+"s", termino+"es", termino+"ing"]:
                found = True
                print(strings.yesTerm)
                break
            
        #if the term is not found the user decides to include it or not
        if not found:
            print(strings.noTerm)
            add = str(input(strings.addTerm))
            if add.upper() == 'Y':
                gp.add(term)
                glossary = refreshGlossary()
                print(f'The term "{term}" has been added.\n')
            else: print(f'The term "{term}" has not been added.\n')
        fun.pressEnter()
        fun.clear()
        
#refresh the glossary
def refreshGlossary(): return gp.run()
        
if __name__ == "__main__":
    glossaryManagerSD()