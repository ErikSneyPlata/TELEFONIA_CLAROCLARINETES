import json
def lecturaArchivos(ruta): #recibe la ruta del archivo a leer
    with open(ruta, encoding='utf-8') as mostrar:
        print(mostrar.read())

def input_opcion():
    n = int(input("ingrese la opcion: "))
    return n
    
def interlineado():
    ruta="ARCHIVOS\\interlineado.txt"
    lecturaArchivos(ruta)
    
def leer_crear_json():
    try:
        with open("json\\datos.json","r") as lectura:
            datos = json.load(lectura)
            return datos
    except FileNotFoundError:
        datos=[]
        return datos

def guardar_actualizar_json(datos):
    with open("json\\datos.json","w") as guardar:
        json.dump(datos,guardar, indent=4)
    print("\nGUARDANDO...\n")
        
    
        


    
#--------------------------------------------------------------------------------    
def agregar_usuario():
    nombre=input("ingrese el nombre: ")
    documento=input("ingrese el documento: ")
    edad=input("ingrese la edad: ")
    direccion=input("Ingrese la direccion: ")
    ciudad=input("ingrese la ciudad: ")
    categoria_cliente=input("ingrese la categoria: ")
    usuario={
        "nombre":nombre,
        "documento":documento,
        "edad":edad,
        "direccion":direccion,
        "ciudad":ciudad,
        "categoria": categoria_cliente,
        "contrasena":"",      
    }
    datos = leer_crear_json()
    datos.append(usuario)
    guardar_actualizar_json(datos)
    print("\nusuario agregado con exito\n")
    
def modificar_usuario():
    while True:
        datos = leer_crear_json()
        mapeo_por_documento = input("Ingrese el documento del usuario a buscar: ")
        for usuario in datos:
                if usuario["documento"] == mapeo_por_documento:
                    print("\nPROCEDEMOS A MODIFICAR...\n")
                    usuario["nombre"] = input("ingrese el nombre: ")
                    usuario["edad"]=input("ingrese la edad: ")
                    usuario["direccion"]=input("Ingrese la direccion: ")
                    usuario["ciudad"]=input("ingrese la ciudad: ")
                    usuario["categoria"]=input("ingrese la categoria: ")
                    usuario["contrasena"]=input("ingrese la contraseña a cambiar: ")
                    guardar_actualizar_json(datos)
                    print("\nusuario modificado con exito \n")
                    return
        print("\nCLIENTE NO ENCONTRADO")
        return
                    #cierre = False #cierra el while una vez encontrado el usuario
                              
            
def eliminar_cliente():
    while True:
        datos = leer_crear_json()
        mapeo_por_documento = input("Ingrese el documento del usuario a eliminar: ")
        for usuario in datos:
                if usuario["documento"] == mapeo_por_documento:
                    datos.remove()
                    guardar_actualizar_json(datos)
                    return print("\nCLIENTE ELIMINADO CORRECTAMENTE")
        return print("El usuario no se encontro")

#2 perfiles de usuarios 
def mostrar_usuarios():
    with open("json\\datos.json","r") as lectura:
            datos = json.load(lectura)
    for usuario in datos:
        for clave,valor in usuario.items():
            print(f"{clave}: {valor}")
        print("\n")

#3 facturas, se hace despues de que se haga el modulo de ventas
def facturas():
    print("FACTURAS")

#4 pqr
def generar_pqr():
    datos=leer_crear_json()
    
    while True:
        
            persona= input("ingrese el documento para verificar el usuario")
            for usuarios in datos:
                if usuarios["documento"]==persona:
                    print(f"Señor/a {usuarios["nombre"]}\n\nVALIDAREMOS SUS DATOS A CONTINUACION:\n")
                    for clave,valor in usuarios.items():
                        print(f"{clave}: {valor}")
                        
                    print("\nBien, ahora generaremos la peticion, queja o reclamo que necesita: \n")
                    usuarios["pqr"].append(input("ingrese la consulta a realizar: "))
                    print(usuarios["pqr"])
                    guardar_actualizar_json(datos)
                    interlineado()  
                    return "\nCONSULTA AÑADIDA A LA BASE DE DATOS CON EXITO Y SOLUCIONADA\n"
            interlineado()  
            return "\nNo esta registrada en la base de datos o indico el documento incorrectamente\n"
           