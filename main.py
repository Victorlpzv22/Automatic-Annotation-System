import random

#definicion de lectores y escritores
entrada = "input" #str(input("Introduce el nombre del fichero: "))
fich_input =  entrada + ".txt"
fich_output = entrada + ".xml"

f = open(fich_input,'r')
w = open(fich_output, 'w')

#definicion de etiquetas
et_oracion_o="<oracion>\n"
et_oracion_c="</oracion>\n"
et_contenido_o= "    <contenido>"
et_contenido_c= "</contenido>\n"
et_SD_o= "    <SD>"
et_SD_c= "</SD>\n"

#categoria de densidad semantica
sd = ["SD--", "SD-", "SD+", "SD++"]

#limites de densidad
l1=25 # frontera entre SD-- y SD-
l2=50 # frontera entre SD- y SD+
l3=75 # frontera entre SD+ y SD++

#devuelve una oracion categorizada en cuanto a su densidad semansita
def calcular_complejidad(oracion):
    complejidad_n = random.random()*100
    if complejidad_n <l1:
        complejidad = sd[0]
    elif l1 <= complejidad_n <l2:
        complejidad = sd[1]
    elif l2 <= complejidad_n <l3:
        complejidad = sd[2]
    else:
        complejidad = sd[3]
    
    return complejidad

def escribir_xml(oracion, complejidad):
    w.write(et_oracion_o)
    w.write(et_contenido_o + oracion + et_contenido_c)
    w.write(et_SD_o + complejidad + et_SD_c)
    w.write(et_oracion_c)
    
lineas = f.readlines()

for linea in lineas:
    a = linea.split(".")
    for i in range(0, len(a) - 1):
        escribir_xml(a[i], calcular_complejidad(a[i]))

f.close()
w.close()


