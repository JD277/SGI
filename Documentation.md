# Documentación para SGI

##  Estructura del directorio
Los archivos .py están orgaizados de la siguiente forma:
```
SGI/
├── app.py
├── Calendario.py
├── inicio.py
├── main.py
├── metricas.py
├── monitoreo.py
├── objetivo.py
├── pdf.py
├── report.py
├── tablas.py
```

## SGI
El siguiente contenido explicará el funcionamiento del codigo en el directorio `SGI`.
-  Explicación del objetivo del sistema
- Argumentos
- Descripción de cada función del sistema


**Objetivo:** `SGI` integra metodos de Firebase, Matplotlib, Pandas y demás dependencias para llevar a cabo la gestión de una Base de Datos de reportes relacionados con servicios públicos, permitiendo solucionar las incidencias de una forma rápida y eficiente.

---

### **Apartado inicial**

##### Comprende la documentación de los archivos: `inicio.py` y `objetivo.py`

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `inicio()`  | None | None   |Introduce al usuario al sistema, dando una explicación de las funcionalidades y el objetivo del mismo|
| `obj()`   | None   |None|  Muestra en pantalla el objetivo del sistema, los beneficios que ofrece, su importancia y los distintos problemas que busca solucionar|

### **Sistema de Reportes**

##### Comprende la documentación del archivo: `report.py`

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `fecha()`  | None  | `Fecha y hora actuales`  |Obtiene la fecha en la cual se utilice la funcion, en formato: "Year-Month-Day Hours-Minutes-Seconds", y lo devuelve para su posterior almacenado.|
| `generar_numero_reporte(tipo_reporte)`   |  `tipo_reporte`: Variable la cual almacena el tipo de reporte especificado  |Numero de reporte asignado para la avería especificada.| Revisa la base de datos para comprobar el tipo de reporte, posteriormente verifica que no haya sido almacenado previamente, en cuyo caso, le asigna un numero de reporte único y lo retorna|
| `guardar_reporte(datos, tipo_reporte)`   | `datos`: Contiene la información del reporte.<br><br>`tipo_reporte`: Contiene el tipo especifico de reporte de avería  |None| Comprueba que la información del reporte sea correcta, en cuyo caso la almacena en la base de datos.|
| `Campos comunes()`   |None|Datos relevantes para el reporte de avería, como fecha, hora, descripción, etc.| Pide al usuario toda la información relevanta para el reporte, posteriormente almacenandola y retornandola.|
| `validar_datos(tipo_averia, descripcion, ciudad, direccion)`   |`tipo_averia:` Contiene el tipo específico de avería a resolver. <br><br> `descripcion:` Especificaciones acerca del problema <br><br>  `ciudad:` La localización desde la que se hace el reporte <br><br> `direccion:` El sitio en el cual se encuentra la avería |`True` si todos los campos fueron llenados correctamente; de otra forma, `false`.| Comprueba que todos los campos requeridos para el reporte sean llenados correctamente antes de almacenarlos.|
| `generar_reporte(tipo_reporte, opciones_averia)`   |`tipo_reporte`: Contiene el tipo especifico de reporte de avería <br><br>`opciones_averia`:  Contiene las distintas averias que pueden ocurrir |None.| Obtiene la fecha y hora actual, posteriormente procesa la información del reporte, el tipo del mismo, generando un número de reporte, finalmente verifica que los datos sean correctos y en cuyo caso lo almacena y lo muestra al usuario.|
| `mostrar_resumen(datos)`   |`datos`: Contiene la información del reporte|None.|Recopila los datos del reporte generado y los muestra al usuario.|
| `menu()`   |None|None.|Obtiene la fecha y hora actual, crea una interfaz de usuario en la cual se puede escoger el tipo de averia de la cual se desea realizar el reporte.|

### **Módulo Principal**

##### Comprende la documentación de los archivos: `app.py` y `main.py`

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `register_admin(username, password, first_name, last_name, email, id_number)`  | `username`: Nombre que seleccionó el usuario<br><br> `password`: Contraseña del usuario <br><br> `first_name`, `last name`: Nombre y apellido del usuario <br><br> `email`, `id_number`: Datos unicos de contacto | None   |Encripta la contraseña y añade los datos del usuario al apartado "admins" de la Base de Datos|
| `login_admin(username, password)`  |`username`: Nombre que seleccionó el usuario <br><br> `password`: Contraseña del usuario | `True`: Si ambos datos se encuentran en la Base de Datos, de otra forma retorna `False` |Revisa la Base de Datos y verifica que tanto el nombre de usuario como la contraseña se encuentren asignados a un administrador|
| `generate_temp_password(length=8)` | `length`: Tamaño que podrá tener la contraseña, incializado en 8 | Un valor aleatorio, el cual se usa como contraseña temporal  |Toma una serie de valores alfanumericos, que posteriormente retorna de forma aleatoria para ser usados como contraseña temporal|
| `admin_ui()`  | None | None   |Muestra la interfaz de inicio de sesión, en la cual los administradores pueden registrarse, iniciar sesión o recuperar acceso a su cuenta en caso de haber olvidado su contraseña|
| `user_ui()`  | None | None   |Muestra la interfaz de usuario, en la cual los usuarios pueden realizar sus distintas acciones|

---
