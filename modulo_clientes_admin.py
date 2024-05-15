import json
import random
import security

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
    while True:
        try:
            nombre=input("ingrese el nombre: ")
            documento=input("ingrese el documento: ")
            edad=input("ingrese la edad: ")
            direccion=input("Ingrese la direccion: ")
            eleccion = input("\nEscoja la ciudad:\n1.Bucaramanga\n2.Giron\n3.Floridablanca\n4.Piedecuesta\n5.Lebrija\n\nSU ELECCION ES: ")
            if eleccion == 1:
                ciudad = "Bucaramanga"
            elif eleccion == 2:
                ciudad = "Giron"  
            elif eleccion == 3:
                ciudad = "Floridablanca"   
            elif eleccion == 4:
                    ciudad = "Piedecuesta"   
            elif eleccion == 5:
                ciudad = "Lebrija"
            else:
                ciudad="Bucaramanga"
                        
            eleccion = random.randrange(1, 4)
            if eleccion == 1:
                categoria_cliente = "bronce"
            elif eleccion == 2:
                categoria_cliente = "plata"  
            elif eleccion == 3:
                categoria_cliente = "oro"   
        
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
            return
        except Exception as error:
                print("\nla opcion que ingresaste no es valida\n")
                security.manejo_errores(error)
    
# agregar_usuario()  
    
def modificar_usuario():
    while True:
        try:
            datos = leer_crear_json()
            mapeo_por_documento = input("Ingrese el documento del usuario a buscar: ")
            for usuario in datos:
                    if usuario["documento"] == mapeo_por_documento:
                        print("\nPROCEDEMOS A MODIFICAR...\n")
                        usuario["nombre"] = input("ingrese el nombre: ")
                        usuario["edad"]=input("ingrese la edad: ")
                        usuario["direccion"]=input("Ingrese la direccion: ")
                        
                        eleccion = input("\nEscoja la ciudad:\n1.Bucaramanga\n2.Giron\n3.Floridablanca\n4.Piedecuesta\n5.Lebrija\n\nSU ELECCION ES: ")
                        if eleccion == 1:
                            ciudad = "Bucaramanga"
                        elif eleccion == 2:
                            ciudad = "Giron"  
                        elif eleccion == 3:
                            ciudad = "Floridablanca"   
                        elif eleccion == 4:
                                ciudad = "Piedecuesta"   
                        elif eleccion == 5:
                            ciudad = "Lebrija"
                        else:
                            ciudad="Bucaramanga"
                        
                        usuario["ciudad"]=ciudad
                        usuario["contrasena"]=input("ingrese la contraseña a cambiar: ")
                        guardar_actualizar_json(datos)
                        print("\nusuario modificado con exito \n")
                        return
            print("\nCLIENTE NO ENCONTRADO")
            return
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)
                              
            
def eliminar_cliente():
    while True:
        try:
            datos = leer_crear_json()
            mapeo_por_documento = input("Ingrese el documento del usuario a eliminar: ")
            for usuario in datos:
                    if usuario["documento"] == mapeo_por_documento:
                        datos.remove(usuario)
                        guardar_actualizar_json(datos)
                        return print("\nCLIENTE ELIMINADO CORRECTAMENTE")
                    
            return print("El usuario no se encontro")
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)
    

#2 perfiles de usuarios 
def mostrar_usuarios():
    with open("json\\datos.json","r") as lectura:
            datos = json.load(lectura)
    interlineado()
    for usuario in datos:
        for clave,valor in usuario.items():
            print(f"{clave}: {valor}")
        print("\n")
    print("\n\nLo anterior mostrado son los usuarios registrados\n")

#3 facturas, se hace despues de que se haga el modulo de ventas
def facturas():
    print("\nFACTURAS\n\n")
    precio_final=0
    precio_cliente=0
    while True:
        datos = leer_crear_json()
        mapeo_por_documento = input("Ingrese el documento del usuario a buscar: ")
        try:
            for usuario in datos:
                if usuario["documento"] == mapeo_por_documento:
                    print("\nPROCEDEMOS A VERIFICAR LA CUENTA DEL CLIENTE...\n")
                    verificacion = usuario.get("servicios adquiridos")
                    for servicios in verificacion:
                        precio_cliente=float(servicios["precio"])
                        precio_final=precio_final+precio_cliente
                    interlineado()
                    return print(f"Nombre: {usuario["nombre"]}\nDocumento: {usuario["documento"]}\nFactura de servicios: {precio_final}\n")      
            else:
                interlineado()
                return print("\nEL CLIENTE NO SE ENCUENTRA EN EL SISTEMA\n")
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)              

#4 pqr
def generar_pqr():
    datos=leer_crear_json()
    
    while True:
        try:
            persona= input("ingrese el documento para verificar el usuario: ")
            for usuarios in datos:
                if usuarios["documento"]==persona:
                    print(f"Señor/a {usuarios["nombre"]}\n\nVALIDAREMOS SUS DATOS A CONTINUACION:\n")
                    for clave,valor in usuarios.items():
                        print(f"{clave}: {valor}")
                        
                    print("\nBien, ahora generaremos la peticion, queja o reclamo que necesita: \n")
                    usuarios.setdefault("pqr", []).append(input("ingrese la consulta a realizar: "))
                    #print(usuarios["pqr"])
                    
                    guardar_actualizar_json(datos)
                    interlineado()  
                    return "\nCONSULTA AÑADIDA A LA BASE DE DATOS CON EXITO Y SOLUCIONADA\n"
            interlineado()  
            return "\nNo esta registrada en la base de datos o indico el documento incorrectamente\n"
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)
        
           