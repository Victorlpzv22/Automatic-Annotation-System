import numpy as np
import matplotlib.pyplot as plt
import statistics

'''
AUTHORS:    Roberto Ruiz y Víctor López

DATE:       24/04/23

ABOUT:      This module paints the graphs
'''


def fig(fig): plt.figure(fig)

def roundNum(num): return round(num, 3)

def subplot(data_list, num_bins, categorias, titles):
  
    porcentajes = []
    maximosX = []
    maximosY = []
    # Crear la gráfica de barras
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs = axs.flatten()
    fig.suptitle(titles[0])
    
    for i in range(len(data_list)):
        if data_list[i]: 
            maximosX.append(max(data_list[i]))
            media = roundNum(statistics.mean(data_list[i]))
            mediana = roundNum(statistics.median(data_list[i]))
            print(f"{categorias[i].upper()}: the mean is {media} and the median is {mediana}")
        else: print(f"{categorias[i]}: there are no sentences.")            
        
    for i, data in enumerate(data_list):
        if data:
            # Crear histograma de los datos
            counts, bins = np.histogram(data, bins=num_bins, range=(0, max(maximosX)))
            # Obtener el total de valores en la lista
            total = len(data)
            # Calcular el porcentaje de cada rango
            percentages = [count / total * 100 for count in counts]
            porcentajes.append(percentages)
            maximosY.append(max(percentages))
        else:
            porcentajes.append([])
            maximosY.append(0)

    for i, data in enumerate(data_list):
        if data:
            # Graficar el histograma correspondiente
            axs[i].bar(bins[:-1], porcentajes[i], width=bins[1]-bins[0])
            axs[i].set_xlabel(titles[1][i])
            axs[i].set_ylabel(titles[2])
            axs[i].set_title(categorias[i])
            axs[i].set_ylim([0, max(maximosY)])
        else:
            axs[i].set_xlabel(titles[1][i])
            axs[i].set_ylabel(titles[2])
            axs[i].set_title(categorias[i])
    
    fig.tight_layout(pad=1)


    
    



