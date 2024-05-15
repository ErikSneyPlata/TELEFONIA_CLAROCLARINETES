import json
import modulo_clientes_admin
import user as usuarios
    
def security_users():
    datos=modulo_clientes_admin.leer_crear_json()
    modulo_clientes_admin.interlineado()
    corte=True
    while corte:
        print("\n\nBIENVENIDO, ESTE ES EL SISTEMA DE INGRESO PARA USUARIOS\n")
        print("\n\nDesea ingresar? \n1. Si\n2. No\n")
        interaccion = input("Seleccione una opcion: ")
        if interaccion =="1":
            persona=input("ingrese su documento de identificacion para ingresar: ")
            for verificacion in datos:
                if persona == verificacion["documento"]:
                    contraseña =input("Digite la clave (Si es su primera vez ingresando, oprima solo enter): ")
                    if contraseña == verificacion["contrasena"]:
                        usuarios.menu_users(persona)
                    else:
                        return print("\nCONTRASEÑA INCORRECTA\n")
        if interaccion =="2":
            corte=False
            break

            
    