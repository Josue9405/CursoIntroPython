print("Bienvenido")
velAsteroide = int(input("¿A qué velocidad viaja el asteroide?"))
tamAsteroide = int(input("¿Qué tamaño tiene el asteroide en metros?"))
mensaje = "El asteroide"
if(velAsteroide > 25):
    mensaje = " se acerca rápido a "+velAsteroide+"km/s, es un peligro"
    if(tamAsteroide > 25):
        mensaje = mensaje + "\nCausará mucho daño por su tamaño de "+tamAsteroide+" metros"
    else:
        mensaje = mensaje + "\nEs de "+tamAsteroide+"m, se incinerará por la atmosfera"
elif(velAsteroide >= 20):
    mensaje = " generará un rayo"
else:
    mensaje = " no represente ningun peligro"

print(mensaje)