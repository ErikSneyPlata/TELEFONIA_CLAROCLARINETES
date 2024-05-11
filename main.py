import json
import user
import menus_admin
import modulo_clientes_admin as funciones

#menu principal-------------------------------------------------------------------
def menu_pricipal():

    while True:
        ruta_bienvenida ="ARCHIVOS\\bienvenida.txt"
        funciones.lecturaArchivos(ruta_bienvenida)
        opt=int(input("Ingrese una opcion : "))
        try:
            if opt==1:
                menus_admin.menu_admin()
            elif opt==2:
                user.menuUser()
            elif opt==3:
                break  
        except:
            print("\nla opcion que ingresaste no es valida\n")
              
#----------------------------------------------------------------------------------


menu_pricipal()


#REVISAR ELIMINACION NO FUNCIONA CORRECTAMENTE
