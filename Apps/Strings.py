'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       19/04/23

ABOUT:      This script stores the strings of the programm
'''

title='''
  ______               __                                         __      __                 
 /      \             |  \                                       |  \    |  \                
|  $$$$$$\ __    __  _| $$_     ______   ______ ____    ______  _| $$_    \$$  _______       
| $$__| $$|  \  |  \|   $$ \   /      \ |      \    \  |      \|   $$ \  |  \ /       \      
| $$    $$| $$  | $$ \$$$$$$  |  $$$$$$\| $$$$$$\$$$$\  \$$$$$$ \$$$$$$  | $$|  $$$$$$$      
| $$$$$$$$| $$  | $$  | $$ __ | $$  | $$| $$ | $$ | $$ /      $$ | $$ __ | $$| $$            
| $$  | $$| $$__/ $$  | $$|  \| $$__/ $$| $$ | $$ | $$|  $$$$$$$ | $$|  \| $$| $$_____       
| $$  | $$ \$$    $$   \$$  $$ \$$    $$| $$ | $$ | $$ \$$    $$  \$$  $$| $$ \$$     \      
 \$$   \$$  \$$$$$$     \$$$$   \$$$$$$  \$$  \$$  \$$  \$$$$$$$   \$$$$  \$$  \$$$$$$$      
 

  ______                                  __                 __      __                       
 /      \                                |  \               |  \    |  \                      
|  $$$$$$\ _______   _______    ______  _| $$_     ______  _| $$_    \$$  ______   _______    
| $$__| $$|       \ |       \  /      \|   $$ \   |      \|   $$ \  |  \ /      \ |       \   
| $$    $$| $$$$$$$\| $$$$$$$\|  $$$$$$ \$$$$$$    \$$$$$$ \$$$$$$  | $$|  $$$$$$\| $$$$$$$\  
| $$$$$$$$| $$  | $$| $$  | $$| $$  | $$ | $$ __  /      $$ | $$ __ | $$| $$  | $$| $$  | $$  
| $$  | $$| $$  | $$| $$  | $$| $$__/ $$ | $$|  \|  $$$$$$$ | $$|  \| $$| $$__/ $$| $$  | $$  
| $$  | $$| $$  | $$| $$  | $$ \$$    $$  \$$  $$ \$$    $$  \$$  $$| $$ \$$    $$| $$  | $$  
 \$$   \$$ \$$   \$$ \$$   \$$  \$$$$$$    \$$$$   \$$$$$$$   \$$$$  \$$  \$$$$$$  \$$   \$$  


  ______                         __                             
 /      \                       /  |                            
/$$$$$$  | __    __   _______  _$$ |_     ______   _____  ____  
$$ \__$$/ /  |  /  | /       |/ $$   |   /      \ /     \/    \ 
$$      \ $$ |  $$ |/$$$$$$$/ $$$$$$/   /$$$$$$  |$$$$$$ $$$$  |
 $$$$$$  |$$ |  $$ |$$      \   $$ | __ $$    $$ |$$ | $$ | $$ |
/  \__$$ |$$ \__$$ | $$$$$$  |  $$ |/  |$$$$$$$$/ $$ | $$ | $$ |
$$    $$/ $$    $$ |/     $$/   $$  $$/ $$       |$$ | $$ | $$ |
 $$$$$$/   $$$$$$$ |$$$$$$$/     $$$$/   $$$$$$$/ $$/  $$/  $$/ 
          /  \__$$ |                                            
          $$    $$/                                             
           $$$$$$/                                              


Created by Víctor López & Roberto Ruiz.\n'''

selectAnOption = "👇 Please select an option of the ones shown below 👇"

mainMenu = '''\nWelcome to the Automatic Annotation System.\nSave the .xml files in the xml folder and the .txt files in the txt folder.\n\n👇 Please select an option of the ones shown below: 👇\n
    1. SDParser.
    2. SDTranslator. 
    3. SDComparator.
    4. SDStatistics.
    5. SDSentenceStatistics.
    6. SDGlossaryManager.
    7. Help. ❔
    8. Exit. 🚪🏃‍♂️\n'''

helpMenu = '''
    1. About SDParser.
    2. About SDTranslator.
    3. About SDComparator.
    4. About SDStatistics.
    5. About SDSentenceStatistics.
    6. About SDGlossaryManager.
    7. Exit. 🚪🏃‍♂️\n'''

parserMenu = '''\n👇 Please select an option of the ones shown below 👇\n
    1. Parse a XML file to a plain text file.
    2. Exit. 🚪🏃‍♂️
    '''
    
glossayMenu = '''\n👇 Please select an option of the ones shown below 👇\n 
    1. Check if a term is in the Glossary.
    2. Exit. 🚪🏃‍♂️
    '''
    
sentenceMenu = '''\n👇 Please select an option of the ones shown below 👇\n
    1. Analyze the statistics of a sentence.
    2. Exit. 🚪🏃‍♂️
    '''
translatorMenu = '''\n👇 Please select an option of the ones shown below 👇\n
    1. Analyze the Semantic Density of every sentence of a TXT file.
    2. Exit. 🚪🏃‍♂️
    '''
comparatorMenu = '''\n👇 Please select an option of the ones shown below: 👇\n
    1. Compare two XML files.
    2. Exit. 🚪🏃‍♂️
    '''
    
statisticsMenu = '''\n👇 Please select an option of the ones shown below 👇\n
    1. Get the statistics from a XML.
    2. Exit. 🚪🏃‍♂️
    '''

typeOption = "Type a correct option 👉 "

help = ["This app takes a XML file as input and generates a text file with all the content that is inside the label <segment>.",
        "This app takes a text file as input and generates an xml output with the SD level of every sentence.",
        "This app takes two XML files as input and tells the difference between the SD levels.",
        "This app takes a XML file and shows several statistics such as number of verbs, acronyms, tecnicisms and nominal groups acording to the desired SD level.",
        "This app takes a sentence and give you the measured parameters",
        "This app leads to check and add words to the tecnical glossary"]

welcome = {"HelpMenu": "\nWelcome to the Help Menu,\n\n",
           "ParserMenu": "\nWelcome to SDParser,\n",
           "GlossaryMenu": "\nWelcome to SDGlossaryManager,\n",
           "SentenceMenu": "\nWelcome to the SDSentenceStatistics,\n",
           "TranslatorMenu": "\nWelcome to the SDTranslator,\n",
           "ComparatorMenu": "\nWelcome to the SDComparator,\n",
           "StatisticsMenu":"\nWelcome to SDStatistics,\n"}

ciao = "Cya! 🙋‍♂️\n"

xmlInputFile = "Type the name of the input file (Without adding .xml) 👉 "

txtInputFile = "Type the name of the input file (Without adding .txt) 👉 "

txtOutputFile = "Type the name of the output file (Without adding .txt) 👉 "

xmlOutputFile = "Type the name of the output file (Without adding .xml) 👉 "

writeMode = '\nType "Y" if you want to write the output in a .txt log file. (Recommended for long comparisons) 👉 '

errorInputFile = "❌ Error in the input file. Try again.\n"

errorParsing = "\n❌ An error has ocurred trying to parse the XML File"

fileExists = "This file already exists, do you want to overwrite it? (Y/n) 👉 "

typeTerm = "\nWrite the term you want to check 👉 "

typeSentence = '\n👇 Write the sentence you want to get statistics from 👇\n'

yesTerm = "\n✅ The term is in the glossary."

noTerm = '\n❌ The term is not in the list'

addTerm = 'Do you want to add it? (Y/n) 👉 '

separationMode = '''\n👇 Please select a mode to separate the sentences in the TXT file 👇
    1. By lines.
    2. By punctuation symbols [. ? !].
    '''

head_xml = '''<?xml version='1.0' encoding='utf-8'?> 
<document>
    <header>
        <textfile>TITLE</textfile>
        <lang>english</lang>
    </header> \n'''

body_xml_o = "	<body>\n"

body_xml_c = "	</body>\n"

segmento_xml = "	    <segment id='ID' features='semantic-density;SD'>CONTENT</segment>\n" # REEMPLAZAMOS ID, SD Y CONTENT

document_xml = "</document>"

compare1 = "Type the name of the first file to compare (Without adding .xml) 👉 "

compare2 = "Type the name of the second file to compare (Without adding .xml) 👉 "

compareMode = '''
    1. Differences between both files.
    2. All sentences and SD.
    '''
            
errorLength = "\n❌ The length of the XML files doesn't match."

errorCompare = "\n❌ An error has ocurred trying to compare both XML files: "

densityOption = '''\n👇 Please select an option of the ones shown below: 👇\n
            
    1. Show all statistics.
    2. Show statistics for SD++.
    3. Show statistics for SD+.
    4. Show statistics for SD-.
    5. Show statistics for SD--.\n'''
    
closeWindow = "\n❌ Close the windows to continue the program."

files = "\nFile 1    File 2    Sentence\n"