
age1 = int(input("Cuál es tu edad?: "))
name1 = input("Cuál es tu nombre?: ")

age2 = int(input("Cuál es tu edad?: "))
name2 = input("Cuál es tu nombre?: ")

if age1 > age2:
    print(name1 + " es mayor que " + name2)
elif age1 < age2:
    print(name2 + " es mayor que " + name1)
else:
    print("Ambos tienen la misma edad.")
