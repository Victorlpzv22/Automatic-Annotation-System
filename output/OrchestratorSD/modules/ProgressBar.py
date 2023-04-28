import threading
import progressbar
import time


'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This class shows the loading print
'''

class ProgressBar:
    def __init__(self):
        self.hilo = threading.Thread(target=self.mi_funcion)
        self.pausar = False
       
    def mi_funcion(self):
        print("\n")
        widgets = ['Loading: ', progressbar.AnimatedMarker()]
        bar = progressbar.ProgressBar(widgets=widgets).start()
        i = 1
        while not self.pausar:
            time.sleep(0.1)
            bar.update(i)
            i+=1
        bar.finish()
    
    def start(self): self.hilo.start()
        
    def stop(self):
        self.pausar=True
        self.hilo.join()
        print("\nDone!  👍\n")