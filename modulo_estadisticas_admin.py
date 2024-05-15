import json
import modulo_clientes_admin as modulo_clientes 
import modulo_ventas_admin as modulo_ventas


def preferencias_clientes():
    datos_ventas = modulo_clientes.leer_crear_json()
    ventas_servicios = {}
    ventas_productos = {}

    for usuario in datos_ventas:
            for servicio in usuario.get("servicios adquiridos", []) + usuario.get("servicios_adquiridos", []):
                nombre_servicio = servicio["nombre del servicio"]
                ventas_servicios[nombre_servicio] = ventas_servicios.get(nombre_servicio, 0) + 1
                
            for producto in usuario.get("productos adquiridos", []) + usuario.get("productos_adquiridos", []):
                nombre_producto = producto.get("nombre del producto", producto.get("nombre del servicio"))
                ventas_productos[nombre_producto] = ventas_productos.get(nombre_producto, 0) + 1

    servicio_mas_vendido = max(ventas_servicios, key=ventas_servicios.get)
    producto_mas_vendido = max(ventas_productos, key=ventas_productos.get)
    modulo_clientes.interlineado()
    print("El servicio más vendido es: ", servicio_mas_vendido)
    print("El producto más vendido es: ", producto_mas_vendido,"\n\n")
    return
                    
              
#2   
def tipos_clientes():
    cont_bronce,cont_plata,cont_oro=0,0,0
    
    datos = modulo_clientes.leer_crear_json()
    for tipo in datos:
        if tipo["categoria"] == "bronce":
            cont_bronce +=1
        elif tipo["categoria"] == "plata":
            cont_plata +=1
        elif tipo["categoria"] == "oro":
            cont_oro +=1
    conteo = (cont_bronce,cont_plata,cont_oro)
    # cont_bronce,cont_plata,cont_oro = sorted(conteo, reverse=True)
    # print(cont_bronce,cont_plata,cont_oro)
    modulo_clientes.interlineado()
    print(f"BRONCE: {cont_bronce}\nPLATA: {cont_plata}\nORO: {cont_oro}\n\n")
            
            
        

#4
def areas_geograficas():
    modulo_clientes.interlineado()
    ciudades = []
    print("areas geograficas donde mas se venden los servicios")
    datos = modulo_clientes.leer_crear_json()
    for area in datos:
        ciudades.append(area["ciudad"])
        
    contador_ciudades = {}
    for ciudad in ciudades:
        if ciudad in contador_ciudades:
            contador_ciudades[ciudad] += 1
        else:
            contador_ciudades[ciudad] = 1
            
    max_frecuencia = max(contador_ciudades.values())
    ciudades_repetidas=[]
    for ciudad,frecuencia in contador_ciudades.items():
        if frecuencia == max_frecuencia:
            ciudades_repetidas.append(ciudad)
        
    print("Ciudades repetidas:\n")
    for ciudad in ciudades_repetidas:
        print(f"{ciudad}: {contador_ciudades[ciudad]} veces")
       