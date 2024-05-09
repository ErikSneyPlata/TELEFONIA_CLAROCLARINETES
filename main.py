import json

from admin import *
from user import *

file = open("bienvenida.txt","r")
print(file.read())
file.close()

System = True
while System ==True:
    print("\n")
    menu=int(input("                             Ingrese su eleccion: "))
    if menu == 1:
        print(" ")
    elif menu == 2:
        print(" ")
    elif menu == 3:
        print(" ")
    else:
        print("\n-------------------------Por favor ingresa una opcion valida-------------------------------")
        