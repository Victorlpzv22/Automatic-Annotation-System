import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from matplotlib import pylab
import modules.NounPhrases as np
import modules.Technicism as tec
import modules.Acronyms as acr
import modules.Verbs as verb
import modules.NounPerVerb as NounPerVerb
import modules.Graphs as gra
import modules.ProgressBar as ProgressBar
import modules.GlossaryParser as gp
import Apps.Strings as strings
import Apps.Functions as fun

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script shows statistics and graphs of the parameters and semantic densities of a XML file
'''

def statisticsSD():
    exit = False
    
    while not exit:
        fun.clear()
        print(strings.welcome.get('StatisticsMenu'))
        print(strings.statisticsMenu)
        
        if fun.inputOption(1, 2, strings.typeOption) == 2:  
            exit = True
            fun.clear()
            break
           
        fun.clear()
        print(strings.welcome.get('StatisticsMenu'))

        error = True
        while error:
                try:
                    input1 = fun.openFile("xml")
                    tree = ET.parse(input1)
                    error = False
                except:
                    print(strings.errorInputFile)
                    fun.showFiles("xml")
        root = tree.getroot()

        print(strings.densityOption)
        option = fun.inputOption(1, 5, strings.typeOption)

        #begining progressBar
        progressBar = ProgressBar.ProgressBar()
        progressBar.start()

        if option == 1: #shows all the graphs
            (listNPV, bigListTecs, bigListAcr, bigListVerbs, bigListNounPh) = analyze(option, root)
            progressBar.stop() #ending progressbar
            graphs(listNPV, bigListTecs, bigListAcr, bigListVerbs, bigListNounPh)
        else:#shows one semantic density
            (sd, listNounPhrase, listTecs, listNPV, listAcr) = analyze(option, root)
            progressBar.stop()
            print(f"\n{sd.upper()}:")
            try:
                graph(sd, listNounPhrase, listTecs, listNPV, listAcr)
            except:
                print(f"This XML file has 0 sentences with {sd.upper()}.")
                
#refresh the glossary
def refreshGlossary(): return gp.run()

#populate the lists with the parameters
def analyze(modo, root) -> tuple:
    glossary = refreshGlossary()
    bigListTecs, bigListAcr, bigListNounPh, bigListVerbs, listNPV = [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]
    if modo == 1:
        index = 0
        for segment in root.iter('segment'):
            (nounPhrase, npv, tecnicisms, verbs, acronyms) = extract(segment.text, glossary)
            if segment.attrib.get('features') == f'semantic-density;sd++': index = 0  
            elif segment.attrib.get('features') == f'semantic-density;sd+': index = 1
            elif segment.attrib.get('features') == f'semantic-density;sd-': index = 2
            else: index = 3

            bigListNounPh[index].append(nounPhrase)
            listNPV[index].append(npv)
            bigListTecs[index].append(tecnicisms)
            bigListVerbs[index].append(verbs)
            bigListAcr[index].append(acronyms)

        return (listNPV, bigListTecs, bigListAcr, bigListVerbs, bigListNounPh)
    else:
        listNounPhrase, listTecs, listNPV, listAcr = [], [], [], []
        if modo == 2:
            sd = "sd++"
        elif modo == 3:
            sd = "sd+"
        elif modo == 4:
            sd = "sd-"
        elif modo == 5:
            sd = "sd--"
        for segment in root.iter('segment'):
            if segment.attrib.get('features') == f'semantic-density;{sd}':
                (nounPhrase, npv, tecnicisms, verbsUnused, acronyms) = extract(segment.text, glossary)
                listNounPhrase.append(nounPhrase)
                listTecs.append(tecnicisms)
                listNPV.append(npv)
                listAcr.append(acronyms)

        return (sd, listNounPhrase, listTecs, listNPV, listAcr)

#calculate the parameters of a sentence
def extract(oracion, glossary):
    if oracion:
        nounPhrase = np.noun_phrases(oracion)
        if verb.count_verbs(oracion) > 0: npv = NounPerVerb.nounperverb(oracion)
        else: npv = 1
        tecnicisms = tec.technicism(oracion, glossary)[0]
        verbs = verb.count_verbs(oracion)/len(oracion.split())
        acronyms = acr.count_acronyms(oracion)
    return (nounPhrase, npv, tecnicisms, verbs, acronyms)

#shows the graphs of every semantic density       
def graphs(listNPV, bigListTecs, bigListAcr, bigListVerbs, bigListNounPh):
    print("\nTECNICISM:")
    gra.subplot(bigListTecs, 200, ["SD++",  "SD+", "SD-", "SD--"], ['Appearances of TECNICISM per word in the text', ['tecnicism/word', 'tecnicism/word', 'tecnicism/word', 'tecnicism/word'], '% in text']) 
    pylab.gcf().canvas.manager.set_window_title("TECNICISM")
    print("\nVERB:")
    gra.subplot(bigListVerbs, 200, ["SD++",  "SD+", "SD-", "SD--"], ['Appearances of VERB per word in the text', ['verb/word', 'verb/word', 'verb/word', 'verb/word'], '% in text'])
    pylab.gcf().canvas.manager.set_window_title("VERB")
    print("\nNOUN PHRASE:")
    gra.subplot(bigListNounPh, 200, ["SD++",  "SD+", "SD-", "SD--"], ['Appearances of NOUN PHRASE per word in the text', ['noun phrase/word', 'noun phrase/word', 'noun phrase/word', 'noun phrase/word'], '% in text'])
    pylab.gcf().canvas.manager.set_window_title("NOUN PHRASE")
    print("\nACRONYM:")
    gra.subplot(bigListAcr, 200, ["SD++",  "SD+", "SD-", "SD--"], ['Appearances of ACRONYM per word in the text', ['acronym/word', 'acronym/word', 'acronym/word', 'acronym/word'], '% in text'])
    pylab.gcf().canvas.manager.set_window_title("ACRONYM")
    print("\nNOUN/VERB:")
    gra.subplot(listNPV, 200, ["SD++",  "SD+", "SD-", "SD--"], ['Appearances of NOUNS per VERB in the text', ['noun/verb', 'noun/verb', 'noun/verb', 'noun/verb'], '% in text'])
    pylab.gcf().canvas.manager.set_window_title("NOUN/VERB")
    print("\nClose the windows to continue the program.")
    plt.show()
 
#show the graph of one semantic density   
def graph(sd, listNounPhrase, listTecs, listNPV, listAcr):
    gra.subplot([listTecs, listAcr, listNPV, listNounPhrase], 200, ["Tecnicism",  "Acronym", "Noun/Verb", "Noun Phrase"], [f"Semantic Density Level: {sd.upper()}", ['tecnicism/word', 'acronym/word', 'verb/word', 'noun phrase/word'], '% in text'])
    pylab.gcf().canvas.manager.set_window_title(sd.upper())
    print(strings.closeWindow)
    plt.show()

if __name__ == "__main__":
    statisticsSD()

