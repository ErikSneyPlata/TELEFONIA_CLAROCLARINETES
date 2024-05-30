import modulo_clientes_admin as reutilizar
import modulo_ventas_admin as reutilizar_ventas
import modulo_estadisticas_admin as reutilizar_estadisticas
import security


#----------------------------------------------------------------------------------
#FUNCIONES DE MENUS PARA ADMIN
def menu_admin():
    while True:
        archivo = "ARCHIVOS//admin_index.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                menuAdminVentas()
            elif opt==2:
                menuAdminClientes()
            elif opt==3:
                estadistica()
            elif opt==4:
                return
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)

            
 
 
 #ventas  
def menuAdminVentas():
    while True:
        archivo = "ARCHIVOS//admin_ventas.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                reutilizar_ventas.mostrar_productos()
            elif opt==2:
                reutilizar_ventas.mostrar_servicios()
            elif opt==3:
                reutilizar_ventas.registro_venta()
            elif opt==4:
                reutilizar_ventas.menu_modficacion_registro_PS()
            elif opt==5:
                return 
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)
            


#cliente
def menuAdminClientes():
    while True:
        archivo = "ARCHIVOS//admin_clientes.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                gestion_usuario()
            elif opt==2:
                reutilizar.mostrar_usuarios()
            elif opt==3:
                reutilizar.facturas()
            elif opt==4:
                reutilizar.generar_pqr()  
            elif opt==5:
                return 
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)

#1 menu de gestion de usuario
def gestion_usuario():
    while True:
        print("\n--------------------------------------------------------\n                   Ingresaste a GESTION DE USUARIOS")
        print("                   1. Registro usuario")
        print("                   2. modificacion de usuario")
        print("                   3. eliminacion de usuario")
        print("                   4.regresar\n")
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                reutilizar.agregar_usuario()
            elif opt==2:
                reutilizar.modificar_usuario()
            elif opt==3:
                reutilizar.eliminar_cliente()
            elif opt==4: 
                return
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)
 

#estadisticas menu estadisticas
def estadistica():
    while True:
        archivo = "ARCHIVOS//admin_estadisticas.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                reutilizar_estadisticas.preferencias_clientes()
            elif opt==2:
                reutilizar_estadisticas.tipos_clientes()
            elif opt==3:
                reutilizar_ventas.manejar_totales_ventas()
            elif opt==4:
                reutilizar_estadisticas.areas_geograficas()  
            elif opt==5:
                return  
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            security.manejo_errores(error)

    

    
    
   
        
     
