#Interesting facts about the Moon. 
#The Moon is Earth's only satellite. 
#There are several interesting facts about the Moon and how it affects life here on Earth.
#On average, the Moon moves 4cm away from the Earth every year. 
#This yearly drift is not significant enough to cause immediate effects on Earth. 
#The highest daylight temperature of the Moon is 127 C.

# Ejercicio uno
from re import template


texto = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
partes = texto.split(".")
palabrasClave = ["average","temperature","distance"]
for parte in partes:
    for palabra in palabrasClave:
        if (parte.find(palabra) > 0):
            if parte.endswith("C"):
                print(parte.strip().replace("C","Celcius"))
            else:
                print(parte.strip())

#Ejercicio dos
print(" ")
titulo = "Datos de la gravedad de {0}\n"
datos = """-------------------------------------------------------------------------------
Nombre del planeta: {1}
Gravedad en {0}: {2}
"""
plantilla = titulo+datos
planeta = "Tierra"
nombre = "Luna"
gravedad = 0.00162 # en kms
print(plantilla.format(nombre,planeta,gravedad*1000))
#Nuevos datos
planeta = "Marte"
nombre = "Ganímedes"
gravedad = 0.00143
print(plantilla)
#Nuevo format
print(plantilla.format(nombre,planeta,gravedad*1000))

