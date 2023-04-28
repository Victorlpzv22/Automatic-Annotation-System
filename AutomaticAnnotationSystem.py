import Apps.ParserSD
import Apps.TranslatorSD, Apps.ComparatorSD, Apps.StatisticsSD, Apps.GlossaryManagerSD, Apps.SentenceStatisticsSD
import Apps.Strings as strings
import Apps.Functions as fun

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script contains the main menu of the programm and the help menu
'''

def orchestratorSD():
    exit = False
    while exit == False: #Repeat until choose exit
        fun.clear()

        print(strings.title)    
        print(strings.mainMenu)

        option = fun.inputOption(1, 8, strings.typeOption)

        #Choose the application
        if option == 1: Apps.ParserSD.parserSD()
        elif option == 2: Apps.TranslatorSD.translatorSD()
        elif option == 3: Apps.ComparatorSD.comparatorSD()
        elif option == 4: Apps.StatisticsSD.statisticsSD()
        elif option == 5: Apps.SentenceStatisticsSD.sentenceStatisticsSD()
        elif option == 6: Apps.GlossaryManagerSD.glossaryManagerSD()
        elif option == 7: helpMenuSD()
        else:
            exit = True
            fun.clear()
            print(strings.ciao)
            
def helpMenuSD():
    fun.clear()

    suboption = 0
    while suboption != 7:  #Repeat until choose exit
        print(strings.welcome.get("HelpMenu"))
        print(strings.selectAnOption)
        print(strings.helpMenu)

        suboption = fun.inputOption(1, 7, strings.typeOption)
        
        fun.clear()

        #Choose the help string 
        if suboption == 1: print(strings.help[0]) 
        elif suboption == 2: print(strings.help[1]) 
        elif suboption == 3: print(strings.help[2])
        elif suboption == 4: print(strings.help[3])  
        elif suboption == 5: print(strings.help[4])
        elif suboption == 6: print(strings.help[5])
        else: pass

if __name__ == "__main__":
    orchestratorSD()