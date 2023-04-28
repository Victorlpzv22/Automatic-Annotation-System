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

selectasAnOption = "👇 Please select an option of the ones shown below 👇"

typeOption= "Type a correct option 👉 "

help = ["This app takes a XML file as input and generates a text file with all the content that is inside the label <segment>.",
         "This app takes two XML files as input and tells the difference between the SD levels.",
         "This app takes a XML file and shows several statistics such as number of verbs, acronyms, tecnicisms and nominal groups acording to the desired SD level.",
         "This app takes a sentence and give you the measured parameters",
         "This app leads to check and add words to the tecnical glossary"]

welcome = {"HelpMenu" : "\nWelcome to the Help Menu,\n",
            }

