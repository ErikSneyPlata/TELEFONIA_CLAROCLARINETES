import json
import user
import menus_admin
import modulo_clientes_admin as funciones_cliente
import security

#menu principal-------------------------------------------------------------------

while True:
    ruta_bienvenida ="ARCHIVOS//bienvenida.txt"
    funciones_cliente.lecturaArchivos(ruta_bienvenida)
    try:
        opt=int(input("Ingrese una opcion : "))
        if opt==1:
            menus_admin.menu_admin()
        elif opt==2:
            security.security_users()
        elif opt==3:
            break  
    except Exception as e:
        security.manejo_errores(e)
              
#----------------------------------------------------------------------------------



