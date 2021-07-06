def divide_elemtnos_de_lista(lista, divisor):
    try:  #programación defensiva
        return [i / divisor for i in lista]  #list comprehension
    except ZeroDivisionError as e:
        print(e) #Uso del print stament
        return lista

lista = list(range(10))
divisor = 0

print (divide_elemtnos_de_lista(lista, divisor))