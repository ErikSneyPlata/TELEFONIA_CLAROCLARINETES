def lecturaArchivos(ruta): #recibe la ruta del archivo a leer
    with open(ruta, encoding='utf-8') as mostrar:
        print(mostrar.read())

def input_opcion():
    n = int(input("ingrese la opcion: "))
    return n
    
def interlineado():
    ruta="ARCHIVOS\\interlineado.txt"
    lecturaArchivos(ruta)