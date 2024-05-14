import modulo_clientes_admin as modulo_clientes 
import modulo_ventas_admin as modulo_ventas

"""
def preferencias_clientes():
    while True:
        datos = modulo_clientes.leer_crear_json()
        print("\nSE VA A ANALIZAR LAS PREFERENCIAS DE COMPRAS DE LOS CLIENTES")
        for usuario in datos:
            usuario.get("productos adquiridos")
            if valor == True:
                        for i in valor:
                            if 
                    
            
                #if valor["codigo del servicio"] == True:
            print("\n")
        return
                    
preferencias_clientes()                  
      """
#2   
def tipos_clientes():
    print("mirar los tipos de clientes y hacer una estadistica")
    
#3   menu -> estadisticas -> estadisticas de ventas:
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
