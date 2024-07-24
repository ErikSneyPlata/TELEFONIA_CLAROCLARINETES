# Claroclarinetes - Base de Datos de Telefonía

## Descripción

Claroclarinetes es una aplicación desarrollada en Python que proporciona una solución completa para la gestión de datos en la empresa de telefonía del mismo nombre. La aplicación maneja el registro de clientes, la venta de servicios y productos, y el manejo de facturas. Además, ofrece un módulo de estadísticas para facilitar el análisis de ventas y la identificación de tendencias.

## Funcionalidades

### Registro de Clientes
- **Agregar Clientes**: Permite añadir nuevos clientes a la base de datos.
- **Buscar Clientes**: Facilita la búsqueda de clientes mediante filtros como nombre, ID, o correo electrónico.
- **Actualizar Información**: Permite modificar la información existente de un cliente.
- **Eliminar Clientes**: Opción para eliminar registros de clientes que ya no se necesiten.

### Venta de Servicios y Productos
- **Registro de Ventas**: Registra cada transacción de venta de servicios o productos.
- **Actualizar Ventas**: Permite modificar los detalles de una venta registrada.
- **Eliminar Ventas**: Opción para eliminar registros de ventas no deseados.

### Manejo de Facturas
- **Generar Facturas**: Crea facturas detalladas para cada venta realizada.
- **Consultar Facturas**: Permite a los clientes y administradores consultar facturas generadas.
- **Actualizar Facturas**: Modifica los detalles de las facturas cuando sea necesario.

### Estadísticas
- **Ventas por Ciudad**: Muestra estadísticas detalladas sobre las ventas en diferentes ciudades.
- **Productos Más Comprados**: Proporciona información sobre los productos más populares.
- **Ventas Totales**: Ofrece un resumen de las ventas totales realizadas en un periodo específico.

## Estructura del Menú

### Menú de Ingreso

1. **Admin**
   - **Gestión de Clientes**: Añadir, buscar, actualizar y eliminar clientes.
   - **Gestión de Ventas**: Registrar, actualizar y eliminar ventas.
   - **Gestión de Facturas**: Generar, consultar y actualizar facturas.
   - **Estadísticas**: Visualizar reportes y estadísticas sobre ventas y productos.

2. **Usuario**
   - **Consulta de Productos y Servicios**: Ver los productos y servicios disponibles.
   - **Registro de Ventas**: Registrar ventas de productos y servicios.
   - **Consulta de Facturas Personales**: Consultar las facturas generadas para su cuenta.

## Requisitos

- **Python**: La aplicación requiere Python 3.x para ejecutarse.
- **Dependencias**: Asegúrate de tener las siguientes bibliotecas instaladas:
  - `json` (para manejo de archivos JSON)
  - `os` (para operaciones del sistema operativo)

## Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/claroclarinetes.git



## Uso

### Ingreso

Cuando inicies la aplicación, se te presentará una pantalla de ingreso donde podrás elegir entre dos roles: **Admin** o **Usuario**.

1. **Admin**:
   - **Gestión de Clientes**: Los administradores tienen acceso completo para añadir, buscar, actualizar y eliminar clientes.
   - **Gestión de Ventas**: Los administradores pueden registrar, actualizar y eliminar ventas. También pueden ver un historial completo de todas las transacciones.
   - **Gestión de Facturas**: Los administradores pueden generar nuevas facturas, consultarlas y actualizar detalles si es necesario.
   - **Estadísticas**: Los administradores pueden acceder a las estadísticas de ventas, incluyendo datos por ciudad, productos más comprados y ventas totales.

2. **Usuario**:
   - **Consulta de Productos y Servicios**: Los usuarios pueden ver una lista de productos y servicios disponibles para la compra.
   - **Registro de Ventas**: Los usuarios pueden registrar ventas de productos y servicios, asociando las ventas con clientes existentes.
   - **Consulta de Facturas Personales**: Los usuarios pueden consultar sus propias facturas generadas a partir de las ventas realizadas.

### Flujo de Trabajo

1. **Inicio de Sesión**:
   - Abre la aplicación y selecciona tu rol: Admin o Usuario.
   - Introduce las credenciales necesarias para acceder al sistema.

2. **Operaciones de Admin**:
   - **Añadir un Cliente**:
     1. Navega a la sección de gestión de clientes.
     2. Rellena el formulario con la información del cliente.
     3. Guarda los cambios.
   - **Registrar una Venta**:
     1. Accede a la sección de ventas.
     2. Introduce los detalles de la venta, incluyendo el cliente y los productos.
     3. Guarda la venta y genera la factura correspondiente.
   - **Ver Estadísticas**:
     1. Dirígete a la sección de estadísticas.
     2. Selecciona el tipo de reporte que deseas visualizar (ventas por ciudad, productos más comprados, etc.).

3. **Operaciones de Usuario**:
   - **Consultar Productos y Servicios**:
     1. Navega a la sección de consulta de productos.
     2. Explora la lista de productos y servicios disponibles.
   - **Registrar una Venta**:
     1. Accede a la sección de registro de ventas.
     2. Introduce los detalles de la venta y selecciona el cliente correspondiente.
     3. Guarda la venta y verifica la factura generada.
   - **Consultar Facturas**:
     1. Ve a la sección de facturas.
     2. Consulta las facturas generadas para tu cuenta y verifica los detalles.

### Ejemplos de Uso

#### Ejemplo 1: Añadir un Cliente

1. Inicia sesión como Admin.
2. Selecciona "Gestión de Clientes" en el menú.
3. Completa los campos requeridos en el formulario de adición de clientes.
4. Haz clic en "Guardar" para añadir el cliente a la base de datos.

#### Ejemplo 2: Registrar una Venta

1. Inicia sesión como Admin.
2. Selecciona "Gestión de Ventas" en el menú.
3. Introduce los detalles de la venta, como el cliente, los productos vendidos y el monto total.
4. Haz clic en "Registrar Venta" para almacenar la transacción y generar la factura.

#### Ejemplo 3: Consultar Facturas

1. Inicia sesión como Usuario.
2. Navega a la sección "Consulta de Facturas".
3. Busca y selecciona la factura que deseas revisar.
4. Visualiza los detalles de la factura.

## Estructura de Archivos JSON

- **`clientes.json`**: Contiene la información de los clientes. Cada entrada incluye detalles como nombre, ID, correo electrónico, etc.
- **`ventas.json`**: Almacena registros de ventas. Cada venta incluye información como el cliente, productos vendidos, fecha y monto total.
- **`facturas.json`**: Guarda las facturas generadas, incluyendo detalles sobre la venta y los datos del cliente.
- **`estadisticas.json`**: Archivo que contiene datos recopilados para generar reportes estadísticos sobre ventas y productos.

## Contribución

1. **Haz un Fork del Proyecto**:
   ```bash
   git fork https://github.com/tu_usuario/claroclarinetes.git

2. **Crea una Nueva Rama**:
```bash
git checkout -b feature/nueva-funcionalidad
```
3. **Realiza los Cambios Necesarios**: Modifica o añade el código según sea necesario.
4. **Haz Commit de tus Cambios**:
```bash
git commit -m 'Añadir nueva funcionalidad'
```
5. **Envía los Cambios a tu Fork**:
```bash
git push origin feature/nueva-funcionalidad
```
6. **Crea un Pull Request** en el repositorio original para que tus cambios sean revisados e integrados.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
Para cualquier duda o consulta, puedes ponerte en contacto con el equipo de desarrollo a través del correo electrónico: Eplata391@gmail.com

