import json
import modulo_clientes_admin as funciones_modulo_cliente
import modulo_estadisticas_admin as estadisticas

TS = 0
TP = 0

#estadistica conteo de ventas
def manejar_totales_ventas():
    interlineado()
    print("\n\nVentas totales de servicios:", TS)
    print("Ventas totales de productos:", TP,"\n")
#--------------------------------------------------------------------------
def lecturaArchivos(ruta): #recibe la ruta del archivo a leer
    with open(ruta, encoding='utf-8') as mostrar:
        print(mostrar.read())

def input_opcion():
    n = int(input("ingrese la opcion: "))
    return n

def interlineado():
    ruta="ARCHIVOS\\interlineado.txt"
    lecturaArchivos(ruta)
    
def leer_crear_servicios():
    try:
        with open("json\\ventas.json","r") as lectura:
            datos = json.load(lectura)
            servicios = datos.get("servicios",[])
            return servicios
    except FileNotFoundError:
        return []
    
def leer_crear_productos():
    try:
        with open("json\\ventas.json","r") as lectura:
            datos = json.load(lectura)
            productos = datos.get("productos",[])
            return productos
    except FileNotFoundError:
        return []

def guardar_actualizar_json(servicios, productos):
    datos = {"servicios": servicios, "productos": productos}
    with open("json\\ventas.json", "w") as guardar:
        json.dump(datos, guardar, indent=4)
    print("\nGUARDANDO...\n")

#----------------------------------------------------------------------
#1. mostrar productos
def mostrar_productos():
    productos = leer_crear_productos()
    servicios= leer_crear_servicios()
    while True:
        for especificacion in productos:
            for clave,valor in especificacion.items():
                print(f"{clave}: {valor}")
            print("\n")
        break
#2. mostrar servicios         
def mostrar_servicios():
    servicios = leer_crear_servicios()
    while True:
        for especificacion in servicios:
            for clave,valor in especificacion.items():
                print(f"{clave}: {valor}")
            print("\n")
        break
#3. registro venta         
def registro_venta():
    while True:
        interlineado()
        print("\n1. registrar venta de servicios\n2. registrar venta de productos\n3.ver estudio del cliente automatizado\n4. regresar\n\n")
        try:
                opt=int(input("Ingrese una opcion : "))
                if opt==1:
                    registrando_venta_servicios()
                elif opt==2:
                    registrando_venta_productos()
                elif opt==3:
                    interaccion_cliente()
                elif opt==4:
                    return
        except:
                print("\nla opcion que ingresaste no es valida\n")
#3.1
def registrando_venta_servicios():
    global TS
    datos = funciones_modulo_cliente.leer_crear_json()
    servicios=leer_crear_servicios()
    while True:
        interlineado()
        print("\n¡ingrese el documento del cliente para hacer la busqueda!\n")
        doc=input("Ingrese el documento: ")
        for usuario in datos:
            if usuario["documento"]==str(doc):
                print("\nQue servicio vas a agregar?\n")
                mostrar_servicios()
                servicio=input("ingrese CODIGO del servicio como aparece para agregarlo: ")
                for especificacion in servicios:
                    if servicio == especificacion["codigo del servicio"]:
                        usuario.setdefault("servicios adquiridos",[]).append(especificacion)
                        funciones_modulo_cliente.guardar_actualizar_json(datos)
                        TS+=1 
                        manejar_totales_ventas()
                        return print("\nSERVICIO AÑADIDO CON EXITO AL CLIENTE ", usuario["nombre"], " con identificacion ",usuario["documento"], "\n")                        
                else:
                    return print("SERVICIO NO ENCONTRADO")
        else:
            return print("NO SE ENCONTRO AL CLIENTE")

#3.2                                           
def registrando_venta_productos():
    global TP
    datos = funciones_modulo_cliente.leer_crear_json()
    productos=leer_crear_productos()
    while True:
        interlineado()
        print("\n¡ingrese el documento del cliente para hacer la busqueda!\n")
        doc=input("Ingrese el documento: ")
        for usuario in datos:
            if usuario["documento"]==str(doc):
                print("\nQue producto vas a agregar?\n")
                mostrar_productos()
                producto=input("ingrese CODIGO del servicio como aparece para agregarlo: ")
                for especificacion in productos:
                    if producto == especificacion["codigo del producto"]:
                        usuario.setdefault("productos adquiridos",[]).append(especificacion)
                        funciones_modulo_cliente.guardar_actualizar_json(datos)
                        TP = TP+1
                        manejar_totales_ventas() 
                        return print("\nPRODUCTO AÑADIDO CON EXITO AL CLIENTE ", usuario["nombre"], " con identificacion ",usuario["documento"], "\n")                       
                else:
                    return print("PRODUCTO NO ENCONTRADO")
        else:
            return print("NO SE ENCONTRO AL CLIENTE")

registrando_venta_productos()
#3.3
def interaccion_cliente():
    print("segun las compras anteriores ofrecer")
#4.	Modificar productos y servicios
def menu_modficacion_registro_PS():
    while True:
        interlineado()
        print("\n\n1. registrar un producto\n2. modificar un producto\n\n3. registrar un servicio\n4. modificar un servicio\n5. regresar")
        try:
                opt=int(input("Ingrese una opcion : "))
                if opt==1:
                    registrar_producto()
                elif opt==2:
                    modificar_productos()
                elif opt==3:
                    registrar_servicio()
                elif opt==4:
                    modificar_servicio()
                elif opt==5:
                    return
        except:
                print("\nla opcion que ingresaste no es valida\n")
    
def registrar_servicio():
    nombre_servicio = input("Ingrese el nombre del servicio: ")
    codigo_servicio = input("Ingrese el codigo del servicio: ")
    precio = input("Ingrese la precio: $")
    especificacion = input("Ingrese la especificacion del servicio: ")
    servicio = {
        "nombre del servicio": nombre_servicio,
        "codigo del servicio": codigo_servicio,
        "precio": precio,
        "especificaciones": especificacion   
    }
    servicios = leer_crear_servicios()
    productos = leer_crear_productos()
    servicios.append(servicio)
    guardar_actualizar_json(servicios, productos)
    print("\nServicio agregado con éxito\n")
    
def modificar_servicio():
    servicios = leer_crear_servicios()
    interlineado()
    mostrar_servicios()
    print("LO ANTERIOR MOSTRADO SON LOS SERVICIOS REGISTRADOS\n\nCual servicio quieres modificar?\n")
    selecion = input("ingrese el CODIGO del producto a modificar")
    for servicio in servicios:
        if selecion == servicio["codigo del servicio"]:
            servicio["nombre del servicio"]= input("Ingreses el nuevo NOMBRE del servicio: ")
            servicio["precio"]= input("Ingrese el nuevo PRECIO del servicio: ")
            servicio["especificaciones"]= input("Ingrese las nuevas ESPECIFICACIONES del servcio: ")
            interlineado()
            print("\nGUARDANDO...\n\n\Servicio modificado correctamente\n")
            print("\n el servicio modificado quedo asi:\n")
            for clave,valor in servicio.items():
                print(f"{clave}: {valor}")
            return
        else:
            interlineado()
            print("\nNO SE ENCONTRO EL SERVICIO\n")
            return

def registrar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    codigo_producto = input("Ingrese el codigo del producto: ")
    precio = input("Ingrese la precio: $")
    especificacion = input("Ingrese la especificacion del producto: ")
    producto = {
        "nombre del producto": nombre_producto,
        "codigo del producto": codigo_producto,
        "precio": precio,
        "especificaciones": especificacion   
    }
    servicios = leer_crear_servicios()
    productos = leer_crear_productos()
    productos.append(producto)
    guardar_actualizar_json(servicios, productos)
    print("\nProducto agregado con éxito\n")
       
def modificar_productos():
    productos = leer_crear_productos()
    interlineado()
    mostrar_productos()
    print("LO ANTERIOR MOSTRADO SON LOS SERVICIOS REGISTRADOS\n\nCual servicio quieres modificar?\n")
    selecion = input("ingrese el CODIGO del producto a modificar")
    for producto in productos:
        if selecion == producto["codigo del producto"]:
            producto["nombre del producto"]= input("Ingreses el nuevo NOMBRE del producto: ")
            producto["precio"]= input("Ingrese el nuevo PRECIO del producto: ")
            producto["especificaciones"]= input("Ingrese las nuevas ESPECIFICACIONES del producto: ")
            interlineado()
            print("\nGUARDANDO...\n\n\nProducto modificado correctamente\n")
            print("\n el producto modificado quedo asi:\n")
            for clave,valor in producto.items():
                print(f"{clave}: {valor}")
            return
        else:
            interlineado()
            print("\nNO SE ENCONTRO EL PRODUCTO\n")
            return

                
            