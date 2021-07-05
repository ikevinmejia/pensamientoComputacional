objetivo = int(input("Escoge un número: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta +=1

if respuesta**2 == objetivo:
    print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))
else:
    print(str(objetivo) + " No tiene una raiz cuadrada exacta")