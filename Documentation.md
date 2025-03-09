# Documentación para SGI
##  Estructura del directorio
Los archivos están orgaizados de la siguiente forma:
```
SGI/
├──images
├──modules/
│   ├── database/
│   │       ├──db.manager.py
│   │       ├──estructuras.json
│   │       └──reportsGenerator.py
│   ├── Calendario.py
│   ├── geminiAnalizer.py
│   ├── inicio.py
│   ├── metricas.py
│   ├── monitoreo.py
│   ├── objetivo.py
│   ├── pdf.py
│   ├── report.py
│   └──tablas.py
├── Documentation.md
├── README.md
├── Rules.md
└── main.py
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

### **Generador de reportes**:


##### Comprede la documentación del archivo:
`reportsGenerator.py`

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `generate_random_date()`|None|Un valor de tiempo en días|Se encarga de generar fechas aleatorias entre 2020 y 2023 en formato UNIX|
| `generate_priority(date, description)` |`date`: La fecha de la avería<br><br> `description`: Descripción específica del reporte|Nivel de prioridad (alto/medio/bajo)|Asigna la prioridad en base a la descripción del reporte|
| `generate_report()` |None|Un reporte con todos los datos relevantes de la avería (fecha, hora, ciudad, tipo de avería, prioridad)|Se encarga de generar los reportes|
| `generate_synthetic_reports(quantity=1000)` |`quantity`: La cantidad de reportes a generar, incializada en 1000|None|Se encarga de generar reportes sintéticos|

>## `Monitoreo.py`

| Name         | Args | Return          | Description     |
|--------------|------|--------------|--------------|
| `buscar_reporte(tipo_reporte, numero_reporte)`|  `tipo_reporte`: Un string que indica el tipo de reporte a buscar en la colección.<br><br> `numero_reporte` Un valor que representa el número único del reporte que se desea encontrar:  |None   |Busca un reporte específico en la base de datos utilizando el tipo de reporte y el número de reporte como criterios de búsqueda.|
| `mostrar_reporte(reporte)`   |  `reporte`:Es un  diccionario que contiene los detalles del reporte que se desea mostrar, incluyendo información como el número, fecha, tipo de avería, y más.   |None |  Muestra la información detallada de un reporte encontrado en la interfaz de usuario utilizando Streamlit|
| `crearTextPDF(reporte)`   |`reporte`: Un diccionario que contiene los detalles del reporte del cual se desea generar el texto. |Cadena de texto que contiene la información del número de reporte.|  Crea un texto que representa la información esencial de un reporte, que puede ser utilizado para generar un archivo PDF.|
|` menu() ` |None|None| Crea una interfaz para buscar un reporte por número y tipo, y generar un PDF del reporte encontrado.|


### **Módulo Principal**
#### > Database:
>##### dbmanager.py

| Name         | Args | Return          | Description     |
|--------------|------|--------------|--------------|
| `init`  |`credential`: Ruta a la clave de cuenta de servicio de Firebase (por defecto: `"modules/database/estructuras.json"`). <br></br>`database_url`: URL de la base de datos en tiempo real de Firebase(por defecto: `"https://estructuras-9be66-default-rtdb.firebaseio.com/"`).   | None|Inicializa la conexión con Firebase.  |
|  `unix_to_string_time`   |  `ts`: Marca de tiempo Unix (segundos desde el 1 de enero de 1970).   | Devuelve una cadena en el formato "YYYY - MM - DD HH : MM : SS" o un mensaje de error si ocurre una excepción. |Convierte una marca de tiempo Unix a un formato de cadena legible.   |
|  `write_record`   |  `Data`: Diccionario que contiene la información del informe |    None|  Escribe datos de un informe en la base de datos.  |
|  `read_record`    | None | Devuelve un diccionario que contiene todos los informes, utilizando sus identificadores únicos como claves.|  Lee todos los informes de la base de datos.   |
|  ` update_record `|  `data` : Diccionario que contiene los campos actualizados que se desean modificar en el informe <b></b>`id`: Identificador único del informe que se desea actualizar.  | None |  Actualiza un informe existente en la base de datos. |
| `delete_record`|  `id` :  Identificador único del informe que se desea eliminar.  | None |   Elimina un informe de la base de datos utilizando.|
|  `get_report_by_id`|  `id` :  Identificador único del informe que se desea obtener..  |Devuelve un diccionario que contiene los datos del informe o `None` si no se encuentra el informe con el ID proporcionado. |  Recupera un informe específico de la base de datos utilizando su identificador único.  |
| `get_report_by_city`|  `city  `:  Nombre de la ciudad por la cual se desea filtrar los informes.  | Devuelve una lista de informes que coinciden con la ciudad especificada. |    Recupera informes filtrados por ciudad.  |
| `get_report_by_service`  |  `service `:  Tipo de servicio por el cual se desea filtrar los informes.  |  Devuelve una lista de informes que coinciden con el tipo de servicio especificado. |    Recupera informes filtrados por tipo de servicio.   |
| `get_report_by_priority`   |  `priority `:  Nivel de prioridad por el cual se desea filtrar los informes.  |  Devuelve una lista de informes que coinciden con el nivel de prioridad especificado. |    Recupera informes filtrados por nivel de prioridad.    |
| `get_report_by_date`   |  `date `: Fecha de registro por la cual se desea filtrar los informes (formato YYYY-MM-DD).  |   Devuelve una lista de informes que coinciden con la fecha especificada. |   Recupera informes filtrados por la fecha de registro.   |
|  `get_report_by_date_of_failure`    |  `date `:  Fecha de falla por la cual se desea filtrar los informes (formato YYYY-MM-DD).  |   Devuelve una lista de informes que coinciden con la fecha de falla especificada. |   Recupera informes filtrados por la fecha de falla.   |
|   `get_report_by_street`  |  `street `:  Nombre de la calle por la cual se desea filtrar los informes.  |  Devuelve una lista de informes que coinciden con el nombre de la calle especificado. |    Recupera informes filtrados por el nombre de la calle.     |
|    `search_records`  |  ** Filtros soportados**:<b> </b>**city**: Coincidencia exacta (sin importar mayúsculas o minúsculas) .<b></b>**service**: Coincidencia exacta (sin importar mayúsculas o minúsculas).<b></b>**priority**: Coincidencia exacta (sensible a mayúsculas y minúsculas).<b> </b>**date_of_record**: Coincidencia exacta (formato YYYY-MM-DD). |  Devuelve una lista de informes coincidentes con sus respectivos IDs.|   Realiza búsquedas utilizando consultas nativas de Firebase, lo que es eficiente para conjuntos de datos grandes. |
|  `mark_report_completed`    | `report_id`:ID único del informe que se desea marcar como completado.|   Devuelve `True` si la operación fue exitosa, o `False` en caso contrario.|    Marca un informe como completado y registra la marca de tiempo de finalización.  |
|  `get_completed_reports`    | None|   Devuelve una lista de informes completados junto con sus IDs.|  Recupera todos los informes completados.  |

##### Comprende la documentación de los archivos: `app.py` y `main.py`

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `register_admin(username, password, first_name, last_name, email, id_number)`  | `username`: Nombre que seleccionó el usuario<br><br> `password`: Contraseña del usuario <br><br> `first_name`, `last name`: Nombre y apellido del usuario <br><br> `email`, `id_number`: Datos unicos de contacto | None   |Encripta la contraseña y añade los datos del usuario al apartado "admins" de la Base de Datos|
| `login_admin(username, password)`  |`username`: Nombre que seleccionó el usuario <br><br> `password`: Contraseña del usuario | `True`: Si ambos datos se encuentran en la Base de Datos, de otra forma retorna `False` |Revisa la Base de Datos y verifica que tanto el nombre de usuario como la contraseña se encuentren asignados a un administrador|
| `generate_temp_password(length=8)` | `length`: Tamaño que podrá tener la contraseña, incializado en 8 | Un valor aleatorio, el cual se usa como contraseña temporal  |Toma una serie de valores alfanumericos, que posteriormente retorna de forma aleatoria para ser usados como contraseña temporal|
| `admin_ui()`  | None | None   |Muestra la interfaz de inicio de sesión, en la cual los administradores pueden registrarse, iniciar sesión o recuperar acceso a su cuenta en caso de haber olvidado su contraseña|
| `user_ui()`  | None | None   |Muestra la interfaz de usuario, en la cual los usuarios pueden realizar sus distintas acciones|

>### Metricas.py

| Name         | Args | Return          | Description     |
|--------------|------|--------------|--------------|
| `obtener_reportes  ` |    ` tipo_reporte`: Determina qué colección de reportes se va a acceder en la base de datos.   |   Los datos de todos los documentos en la colección especificada  |  Recupera todos los documentos de una colección en una base de datos y devuelve un DataFrame de pandas con los datos de esos documentos.|
|  ` grafico_reportes_por_ciudad(df) `  |   ` df`: Contiene los datos de reportes, incluyendo una columna ciudad | None | Muestra un gráfico de barras con la cantidad de reportes por ciudad |
|   `grafico_reportes_por_tipo_averia(df) `  |  ` df  `: Contiene una columna llamada tipo_de_averia  |None|  Muestra un gráfico de barras con la cantidad de reportes por tipo de avería|
|  ` grafico_evolucion_temporal(df) `  | ` df`: Contiene una columna llamada fecha_del_reporte | None| Muestra un gráfico de líneas que representa la evolución de reportes a lo largo del tiempo |
|  ` menu() `| None  | None | Crea una interfaz de usuario para el análisis de reportes, permitiendo al usuario seleccionar un tipo de reporte y generando gráficos basados en los datos obtenidos.|


>### Tablas.py

| Name         | Args | Return          | Description     |
|--------------|------|--------------|--------------|
| `mostrar_reportes_como_tabla(tipo_reporte)`  | `tipo_reporte `: Tipo de informacion consultar en la base de datos. | None   |Recupera y muestra los reportes de un tipo específico en formato de tabla utilizando Streamlit.|
|  ` main()` |None | None  |Configura el panel de reportes en una aplicación Streamlit, mostrando imágenes y botones para diferentes tipos de reportes.|

>### geminiAnalizer.py

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `init`  |`api_key`: Clave de API para configurar el acceso (tipo:`str`)  |None|Inicializa la configuración del modelo generativo y establece las variables necesarias. |
| `load_data`  |`data`:  Son Datos provenientes del DbManager, que pueden ser una lista de diccionarios o un diccionario estilo Firebase (tipo: ` list o dict` )|None|Carga datos desde métodos del DbManager, adaptando el formato según sea necesario.|
| `filter_data`   |`date_column`: Nombre del campo de fecha a utilizar (tipo: str, predeterminado: "date_of_record")  <br></br>  `start_date`: Fecha de inicio en formato YYYY-MM-DD (tipo:`Optional[str]` ) <br></br>  `end_date`: Fecha de fin en formato YYYY-MM-DD (tipo:` Optional[str]`)  <br></br> `filters`: Pares campo-valor para realizar coincidencias adicionales (tipo: `kwargs`)| None|Filtra los datos por rango de fechas y/o valores de campo.
| `analyze` | None | Devuelve un diccionario que contiene los resultados del análisis y metadatos, incluyendo: <br></br> `analysis `:Resultados del análisis generado por la IA. <br></br> `record_count`: Cantidad de registros analizados.  <br></br>`time_range:`Rango temporal de los datos (si corresponde).  |Genera un análisis impulsado por IA de los datos filtrados. |


>### Calendario.py 

| **Name**         | **Args** | **Return**          | **Description**     |
|--------------|------|--------------|--------------|
| `obtener_reportes()`  | None  | Lista de diccionarios, cada uno conteniendo los datos de un reporte junto con su tipo. | Recupera todos los reportes de diferentes tipos de una base de datos Firestore.|
| `generar_eventos(reportes)`   |  `reportes`: Lista de diccionarios con información sobre averías (fecha, hora, tipo, prioridad y descripción). |Contiene todos los eventos que se han creado a partir de los reportes procesados.| Convierte una lista de reportes en eventos adecuados para un calendario, asignando colores a cada tipo de reporte.|
| `mostrar_calendario()`   | None   |None|Crea un calendario interactivo para visualizar reportes de averías utilizando Streamlit.|
