import modulo_clientes_admin as reutilizar
#----------------------------------------------------------------------------------
#FUNCIONES DE MENUS PARA ADMIN
def menu_admin():
    while True:
        archivo = "ARCHIVOS\\admin_index.txt"
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
            print("Error: ",error)
            
 
 
 #ventas  
def menuAdminVentas():
    while True:
        archivo = "ARCHIVOS\\admin_ventas.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                productos()
            elif opt==2:
                servicios()
            elif opt==3:
                registro_venta()
            elif opt==4:
                modificacion_PS()  
            elif opt==5:
                return 
        except:
            print("\nla opcion que ingresaste no es valida\n")


#1
def productos():
    print("\nLOS SIGUIENTES PRODUCTOS SON LOS PRODUCTOS DISPONIBLES ACTUALMENTE\n")
#2
def servicios():
    print("\nLOS SIGUIENTES SERVICIOS SON LOS PRODUCTOS DISPONIBLES ACTUALMENTE\n")
#3
def registro_venta():
    while True: 
        print("--------------------------------------------------------\n                   Ingresaste al registro de ventas\n")
        print("                   1. registrar una venta")
        print("                   2. interaccion con claro")
        print("                   3. regresar\n")
        
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                venta_hecha()
            elif opt==2:
                analisis_cliente_venta()
            elif opt==3:
                return
        except:
            print("\nla opcion que ingresaste no es valida\n")
    #3.1 
def venta_hecha():    
    while True: 
        try:
            print("--------------------------------------------------------\n                   ¿Que tipo de venta desea registrar?")
            print("                   1.servicios")
            print("                   2.productos")
            print("                   3.regresar")
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                venta_hecha_servicios()
            elif opt==2:
                venta_hecha_productos()
            elif opt==3:
                return
        except:
            print("\nla opcion que ingresaste no es valida\n")

        #3.1.1
def venta_hecha_servicios():
    print("aqui se meten todas las ventas de servicios al json")
    

        #3.1.2
def venta_hecha_productos():
    print("aqui se meten todas las ventas de productos al json")

    #3.2
def analisis_cliente_venta():
    print("analisis de cliente para una mejor venta extraidos del json")
       
#4
def modificacion_PS():
    while True:
        print("\n--------------------------------------------------------\n                   ¿Que tipo de venta desea registrar?")
        print("                   1.modificar productos")
        print("                   2.modificar servcios")
        print("                   3.regresar\n")
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                modificar_productos()
            elif opt==2:
                modificar_servicios()
            elif opt==3:
                return
        except:
            print("\nla opcion que ingresaste no es valida\n")
    #4.1.
def modificar_productos():
    print("se accede a los productos para modificarlos")
    #4.2
def modificar_servicios():
    print("se accede a los servicios para modificarlos")
    
#cliente
def menuAdminClientes():
    while True:
        archivo = "ARCHIVOS\\admin_clientes.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                gestion_usuario()
            elif opt==2:
                perfiles_usuario()
            elif opt==3:
                facturas()
            elif opt==4:
                pqr()  
            elif opt==5:
                return 
        except:
            print("\nla opcion que ingresaste no es valida\n")

#1
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
                registro_usuario()
            elif opt==2:
                modificacion_usuario()
            elif opt==3:
                eliminar_usuario()
            elif opt==4:
                return 
        except:
            print("\nla opcion que ingresaste no es valida\n")
    #1.1
def registro_usuario():
    print("Se carga el usuario con los datos a el json para añadir sobre otro") #1
    reutilizar.agregar_usuario()
    #1.2
def modificacion_usuario():
    print("Se busca el usuario con los datos a el json para modificarlo sobre el que ya esta") #es mejor eliminarlo y volverlo a colocar
    reutilizar.modificar_usuario()
    #1.3
def eliminar_usuario():
    print("Se busca el usuario con los datos a el json para eliminarlo  sobre otro") #2
    reutilizar.eliminar_cliente()
    
#2
def perfiles_usuario():
    print("Se busca el usuario con los datos a el json para mostrarlo en pantalla sobre el que ya esta") 
    reutilizar.mostrar_usuarios()
#3
def facturas():
    print("mostrar detalle de facturas de cada cliente")
    
#4
def pqr():
    print("genera pqr de un cliente")
    print(reutilizar.generar_pqr())

#estadisticas
def estadistica():
    while True:
        archivo = "ARCHIVOS\\admin_estadisticas.txt"
        reutilizar.lecturaArchivos(archivo)
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                preferencias_clientes()
            elif opt==2:
                tipos_clientes()
            elif opt==3:
                ventas_est()
            elif opt==4:
                areas_geograficas()  
            elif opt==5:
                return  
        except:
            print("\nla opcion que ingresaste no es valida\n")
            
#1
def preferencias_clientes():
    print("analisis de preferencias de los clientes")
#2   
def tipos_clientes():
    print("mirar los tipos de clientes y hacer una estadistica")
#3   
def ventas_est():
    print("--------------------------------------------------------\n                   ANALISIS DE VENTAS HECHAS\n")
    print("                   1. Ventas de servicios")
    print("                   2. Ventas de productos")
    print("                   3.regresar\n")
    while True: 
        try:
            opt=int(input("Ingrese una opcion : "))
            if opt==1:
                analisis_Vservicios()
            elif opt==2:
                analisis_Vproductos()
            elif opt==3:
                return
        except:
            print("\nla opcion que ingresaste no es valida\n")
    #3.1.           
def analisis_Vservicios():
    print("analisis de ventas de SERVICIOS hechas")
    #3.2.
def analisis_Vproductos():
    print("analisis de ventas de PRODUCTOS hechas")

#4
def areas_geograficas():
    print("areas geograficas donde mas se venden los servicios")

    

    
    
   
        
     
