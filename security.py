import json
import modulo_clientes_admin
import user as usuarios
import datetime
import security
    
def security_users():
    datos=modulo_clientes_admin.leer_crear_json()
    modulo_clientes_admin.interlineado()
    corte=True
    while corte:
        try:
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
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)


def manejo_errores(error):
    hora = datetime.datetime.now()
    
    fecha_hora = hora.strftime("%d-%m-%Y %H:%M:%S")
    mensaje_error = f"{fecha_hora}: {error}\n"
    try:
        with open("errores.txt", "a") as archivo:
            archivo.write(mensaje_error)
    except Exception as exc:
        print(f"Error al escribir en el archivo: {exc}")

    