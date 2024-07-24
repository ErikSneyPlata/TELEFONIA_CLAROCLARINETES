Claroclarinetes - Base de Datos de Telefonía

Descripción:

Esta aplicación está diseñada para la empresa Claroclarinetes y proporciona una base de datos para gestionar el registro de clientes, la venta de servicios y productos, y el manejo de facturas. La base de datos se almacena en archivos JSON, y la aplicación también incluye un apartado de estadísticas para analizar las ventas por ciudades y productos más comprados.

Funcionalidades:

  •	Registro de Clientes: Permite añadir, buscar y gestionar información de los clientes.
  •	Venta de Servicios y Productos: Facilita la venta de servicios y productos de la compañía.
  •	Manejo de Facturas: Genera y gestiona facturas por cliente.
  •	Estadísticas: Proporciona estadísticas de ventas, incluyendo:
    o	Ventas por ciudad
    o	Productos más comprados
    o	Ventas totales
    
Estructura del Menú

Menú de Ingreso

  Admin
  o	Gestión de clientes
  o	Gestión de ventas
  o	Gestión de facturas
  o	Visualización de estadísticas

  Usuario
  o	Consulta de productos y servicios
  o	Registro de ventas
  o	Consulta de facturas personales

Requisitos
  •	Python 3.x
  •	Bibliotecas necesarias:
    o	json
    o	os
    
Uso
  1.	Al iniciar la aplicación, se presentará un menú de ingreso para seleccionar entre admin y usuario.
  2.	Según la selección, se mostrarán las opciones correspondientes para gestionar la base de datos o consultar información.
  Estructura de Archivos JSON
    •	clientes.json: Almacena la información de los clientes.
    •	ventas.json: Registra cada venta realizada.
    •	facturas.json: Guarda las facturas generadas por cliente.
    •	estadisticas.json: Contiene datos para las estadísticas de ventas.

Contribución
  1.	Haz un fork del proyecto.
  2.	Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
  3.	Realiza los cambios necesarios y haz commit (git commit -m 'Añadir nueva funcionalidad').
  4.	Envía los cambios a tu fork (git push origin feature/nueva-funcionalidad).
  5.	Crea un Pull Request.

Licencia
  Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
