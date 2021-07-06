# def factorial(n):
#     """Calcula el factorial de n
#     n int > 0
#     returns n!
#     """
#     print(n)
#     if n == 1:
#         return 1
#     return n * factorial (n-1)

# n = int(input("Escribe un entero: "))

# print(factorial(n))

#Diccionarios


""" dict = {x:x**2 for x in range(-10,0) if x%2 ==0}
print(dict)

dict1 = {"a": 1, "b": 2, "c":3, "d":4, "e":5}

# dict = {key:value for (key,value) in dictionary.items()}

triple_dict = {k:v*3 for (k,v) in dict1.items()}
print(triple_dict) """


# Ejercicio diccionario

my_dict = {"Milk": 0.75, "Meat": 10.69, "Eggs": 2.14, "Bread": 1.07}

my_dict2 = {k:v*(19/100)+v for (k,v) in my_dict.items()}

print(f"The old price is: {my_dict}")
print(f"The new price is: {my_dict2}")