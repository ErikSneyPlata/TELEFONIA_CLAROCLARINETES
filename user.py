import modulo_clientes_admin
import modulo_ventas_admin

def menu_users(doc):
    while True:
        archivo = "ARCHIVOS//user_index.txt"
        modulo_clientes_admin.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                    perfil(doc)
            elif opt==2:
                    facturas(doc)
            elif opt==3:
                    consultas(doc)
            elif opt==4:
                    cambiar_pass(doc)  
            elif opt==5:
                    return  
        except:
            print("\nla opcion que ingresaste no es valida\n")


    
def perfil(doc):
    identificacion = doc
    datos=modulo_clientes_admin.leer_crear_json()
    while True:
            for usuarios in datos:
                if usuarios["documento"]==identificacion:
                    print("Señor/a" +usuarios['nombre'] +"\n\nESTA ES LA INFORMACION QUE TENEMOS EN TU PERFIL SOBRE TI\n")
                    for clave,valor in usuarios.items():
                        print(f"{clave}: {valor}") 
                    return 

def facturas(doc):
    identificacion = doc
    print("\nFACTURA\n\n")
    precio_final=0
    precio_cliente=0
    while True:
        datos = modulo_clientes_admin.leer_crear_json()
        try:
            for usuario in datos:
                if usuario["documento"] == identificacion:
                    print("\nPROCEDEMOS A VERIFICAR LA CUENTA DEL CLIENTE...\n")
                    verificacion = usuario.get("servicios adquiridos")
                    for servicios in verificacion:
                        precio_cliente=float(servicios["precio"])
                        precio_final=precio_final+precio_cliente
                    modulo_clientes_admin.interlineado()
                    return print("Nombre: "+usuario['nombre']+"\nDocumento: "+usuario['documento']+"\nFactura de servicios: "+precio_final+"\n")
        except KeyError:
            break 
            
def consultas(doc):
    identificacion = doc
    while True:
        datos = modulo_clientes_admin.leer_crear_json()
        print("Las consultas que has hecho son: ")
        for usuario in datos:
            if identificacion == usuario["documento"]: 
                for valor in usuario["pqr"]:
                    print("Consulta: ",valor)
        return

def cambiar_pass(doc):
    identificacion = doc
    while True:
        datos = modulo_clientes_admin.leer_crear_json()
        for usuario in datos:
                if usuario["documento"] == identificacion:
                    usuario["contrasena"]=input("ingrese la contraseña a cambiar: ")
                    modulo_clientes_admin.guardar_actualizar_json(datos)
                    print("\nCONTRASEÑA MODIFICADA CON EXITO \n")
                    return
        return