# PYTHON

## 1.1 Variables.

### Nombres.
**snake_case** para variables y funciones

**UPPER_SNAKE_CASE** para constantes

Evitar nombres genericos como x, dato.

#### Correcto:
	  edad_usuario = 20

#### Incorrecto:
	  EdadUsuario = 20

## 1.2 Funciones.

### Documentación:

Usar docstrings en formato Google Style:

 	python
  
	def sumatoria(num1,num2):
	  '''Realiza la suma de una serie de numeros
		Args:
			num1, num2: Numeros a sumar
		Returns:
			Suma de ambos numeros'''
		return num1+num2

Usar # para comentarios de una sola línea:

	python
  	
	def sumatoria(num1,num2):
		#Realiza la suma de una serie de numeros
		return num1 + num2	


### Parametros:
Limite maximo de 4 parametros por función. Si hay más, usar **kwargs o clases.

#### Correcto:

	def conectar_db(host, puerto, usuario, contraseña):
	  ...

#### Incorrecto:

	def conectar_db(host, puerto, usuario, contraseña, timeout, ssl,...)
	  ...

## 1.3 Clases y Métodos.

### Nombres:

PascalCase para clases.

snake_case para métodos.

	python
 
	class ProcesadorDatos:
		def __init__(self, datos):
			self.datos = datos

		def limpiar(self):
			'''Limpia los datos'''
			...

Métodos especiales:
Documentar **init**, **str** y métodos mágicos.

	python
 
	class Usuario:
		def __init__(self, nombre, edad):
			'''Constructor de la clase Usuario.'''
			self.nombre = nombre
			self.edad = edad

## 1.4 Errores Comunes a Evitar:

Mutable Defaults:

#### Incorrecto (lista como valor por defecto)

	python
 
	def añadir(valor, inventario = []):
	  inventario.append(valor)

#### Correcto:

	python
 
	def añadir(valor, inventario):
	  inventario = inventario or []
	  inventario.append(valor)

## 1.5 Modularización de Código:

1. Principios Clave:
	##### Single Responsability Principle (SRP): 
	Cada función/clase debe tener una única responsabilidad.
	##### DRY (Don't Repeat Yourself): 
	Evitar código duplicado creando funciones reutilizables.
	##### Abstracción:
	Ocultar detalles complejos detrás de interfaces simples.

2. Estrategias para Dividir Código.
	##### 2.1 Dividir funciones largas:

		Ejemplo Antes:

   		python

		def process_data(raw_data):
			#Paso 1: Limpiar datos
			limpio = []
			for elemento in raw_data:
				if elemento["value"] > 0:
				  ...

			#Paso 2: Calcular metricas
			total = sum(elemento["value"] for elemento in cleaned)
			...

			#Paso 3: Generar reporte
			report = {
				"total": total,
				"average": avg,
				"items": cleaned
				}
			return report

Ejemplo: Despues:

	python
 
	def clean_data(raw_data):
		'''Filtra y limpia los datos crudos.'''
		cleaned = []
		for elemento in raw_data:
			if elemento["value"] > 0:
				...

	def calculate_metrics(data):
		'''Calcula total y promedio'''
		total = sum(elemento["value"] for elemento in data)
		...

	def generate_report(cleaned_data):
		'''Combina datos limpios y metricas'''
		metrics = calculate_metrics(cleaned_data)
		...

	#Uso
	cleaned = clean_data(raw_data)
	report = generate_report(cleaned)

##### 2.2 Crear Clases para Entidades Complejas.

Si un bloque maneja multiples propiedades y comportamientos, usa clases.

Ejemplo:

	python
 
	class DataProcessor:
		def __init__(self, raw_data):
			self.raw_data = raw_data

		def clean(self):
			#Limpia los datos
			self.cleaned_data = [...]

		def calculate_metrics(self):
			#Calcula metricas basicas
			total = sum(elemento["value"] for elemento in self.cleaned_data)
			...

	#Uso
	processor = DataProcessor(raw_data)
	processor.clean()
	report = processor.calculate_metrics()

3, Señales de que un Bloque es Demasiado Grande

##### Longitud: Mas de 30-50 lineas en una funcion.

##### Anidamiento Profundo: Multiples niveles de if/for/try.

##### Comentarios Excesivos: Si necesitas explicar cada seccion con comentarios largos.

##### Dificultad para Hacer Test: Si es complicado escribir pruebas unitarias para el codigo.

# Librerías

## Pillow

### 1.  Modularización de Código

##### Funciones Reutilizables.

**Ejemplo**: Separar operaciones en funciones específicas.

	python
 
	from PIL import Image
	
	def redimensionar(img, ancho, alto):
		#Redimensiona manteniendo relación de aspecto
		return img.resize((ancho,alto))

### 2. Buenas Prácticas

##### 2.1 Validación de Parámetros

	python

	from typing import Tuple
	
	def redimensionar(img, tamaño: Tuple[int,int]):
		if len(tamaño) != 2:
			...
		return img.resize(tamaño)
	
### 3. Ejemplo de Flujo de Trabajo Modular

	python
 
	import cargar_imagen
	import resize
	
	def procesar_imagen(ruta_entrada, ruta_salida):
		#Cargar
		img = cargar_imagen(ruta_entrada)
	
		#Transformar
		img = resize.redimensionar(img, (800,600))
		
		#Guardar
		img.save(ruta_salida, "JPEG", quality = 95)

## Matplotlib

### 1. Reglas de Sintaxis

##### 1.1 Elementos Comunes de Gráficos:

**Titulos y etiquetas:**
	
	ax.set_title("Titulo", fontsize = 14, fontweight = "bold")
	ax.set_xlabel("Eje X", fontsize = 12)
	ax.set_ylabel("Eje Y", fontsize = 12)


**Leyendas:**

	ax.plot(x, y, label = "Serie A")
	ax.legend(loc = "upper right", frameon = false)

**Limites:**

	ax.set_xlim(0, 100)

##### 1.2 Tipos de Gráficos Comunes

**Gráfico de Líneas**

	ax.plot(x, y, color = "#008000", linestyle = "--", linewidth = 2, marker = "o")

**Gráfico de Barras:**

	ax.bar(categorias, valores, color = ["#008000", "#FF0000"], edgecolor = "black")

**Histograma:**

	ax.hist(datos, bins = 20, alpha = 0.7, density = True, edgecolor = "white")

### 2. Buenas Prácticas:

##### 2.1 Cierre de figuras.

Siempre cerrar figuras después de guardar

	python

	fig, ax = plt.subplots()
	ax.plot(x, y)
	plt.savefig("figura.png")
	plt.close()  #Evita fugas de memoria

### 3. Errores Comunes a Evitar.

**No cerrar figuras:** Usar **plt.close()** o el contexto **with**

**Estilos inconsistentes:** Definir un estilo globlal para todo el proyecto.

## Firebase

### 1. Descripcion:

     Es una plataforma de desarrollo de aplicaciones móviles y web creada por Google. Proporciona una variedad de herramientas y servicios que facilitan la creación, implementación y gestión de aplicaciones.   

### 2. Configuración Inicial:

  #### 2.1 Pasos para crear un proyecto en Firebase:
    
  - Ve a la página de Firebase.
  
  - Haz clic en "Ir a la consola".

  - Crear un Proyecto Nuevo**
  
  - Haz clic en "Agregar proyecto" o el botón "+".

-   Configurar el Proyecto.
  - Ingresa un nombre para tu proyecto.
  - Opcional: Habilita Google Analytics.

  - Esperar la Creación del Proyecto
  - Haz clic en "Crear proyecto" y espera unos momentos.

  - Agregar una Aplicación
  - Selecciona la plataforma correspondiente (Android, iOS o Web).

   - Configurar Firebase SDK
   - Copia el fragmento de código proporcionado e intégralo en tu aplicación.

   - Habilitar Servicios Adicionales (Opcional)(cambiar asi)
   - Habilita servicios como Firestore, Authentication, Storage, etc.

### 3. Estructura de la Base de Datos
    
#### 3.1 Como se Organizan los datos:
 
##### Correcto:

##### Estructura Organizada:

     /usuarios
     /usuario1
    {
      "nombre": "Juan",
      "edad": 30,
      "correo": "juan@example.com"
    }
     /usuario2
    {
      "nombre": "María",
      "edad": 25,
      "correo": "maria@example.com"
    }

##### Incorrecto:

##### Estructura plana y desorganizada:

     /datos
     {
    "nombre1": "Juan",
    "edad1": 30,
    "correo1": "juan@example.com",
    "nombre2": "María",
    "edad2": 25,
    "correo2": "maria@example.com"
     }



### 4. Buenas Prácticas:

   #### 4.1 Modelado de Datos:
   

 ##### 4.1.1 Cómo estructurar los datos para optimizar consultas:

  >##### Estrategias:

  - Usar colecciones y documentos.

  - Evitar documentos demasiado grandes. 


 - Indexar campos clave.


  - Estructura relacional vs. no relacional.
  
  
 - Denormalización.
  
  
  - Consulta limitada.
 
 
 -  Filtros y paginación


### 4.2 Seguridad:

 #### 4.2.1 Reglas de uso:

     Permitir el acceso solo a usuarios autenticados 
 
      Restringir el acceso basado en roles de usuario 
 
      Validar datos antes de escribir en la base de datos
  
      Limitar las lecturas y escrituras a rutas específicas
  
      Usar reglas para controlar el acceso a colecciones y documentos
  
      Auditar y revisar regularmente las reglas de seguridad
  
#### 4.2.2  Autenticación y autorización recomendadas:

- >#####  Autenticación por correo electrónico y contraseña: Permite a los usuarios registrarse y acceder  utilizando su dirección de correo electrónico y una contraseña segura.

- > #####  Autenticación con proveedores de terceros: Utiliza autenticación social a través de plataformas como Google, Facebook o Twitter, lo que facilita el acceso a los usuarios al permitirles usar sus cuentas existentes.




### 5. Reglas de Escritura

#### 5.1 Normas sobre cómo escribir código que interactúe con la base de datos:

- ##### Realizar validaciones de datos antes de enviarlos a la base de datos.
  
- ##### Evitar la duplicación de datos innecesaria y mantener una estructura clara. 


> #####  Ejemplo que sigen estas reglas:

    python

     import firebase_admin
     from firebase_admin import credentials, firestore

     # Inicializar la app de Firebase
     cred = credentials.Certificate('ruta/a/tu/archivo/credencial.json')
     firebase_admin.initialize_app(cred)

     # Obtener una referencia a Firestore
       db = firestore.client()

       def obtener_usuarios():
         try:
           usuarios_ref = db.collection('usuarios')
           docs = usuarios_ref.get()

           for doc in docs:
             print(f'{doc.id} => {doc.to_dict()}')

          except Exception as e:
             print(f'Error al obtener usuarios: {e}')

          #Llamar a la función
             obtener_usuarios()

### 6. Ejemplos de Modularización:

 #### 6.1 Estructura del Proyecto:
     /src
    /components
     /services
     /firebase_service.py
    models
    /user_model.py
    /controllers
     /user_controller.py
     
 #### 6.2 Código Modular:

    python

     firebase_service.py
     import firebase_admin
     from firebase_admin import credentials, firestore

    #Inicializa la aplicación de Firebase
     cred = credentials.Certificate('ruta/a/tu/credencial.json')
     firebase_admin.initialize_app(cred)

      db = firestore.client()

      async def get_user(user_id):
      user_ref = db.collection('users').document(user_id)
      user_doc = user_ref.get()
      return user_doc.to_dict() if user_doc.exists else None

     async def add_user(user_data):
     await db.collection('users').add(user_data)
     
 
## Pandas
### 1. General:

#### 1.1 Descripción: 
Es una biblioteca de Python diseñada para la manipulación y análisis de datos. Proporciona estructuras de datos flexibles y eficientes, como DataFrames y Series, que facilitan la limpieza, transformación y análisis de datos
de manera intuitiva.

#### 1.2 Objetivos y beneficios:
     
##### 1.2.1  Objetivos:

- Facilitar la manipulación y análisis de datos.

- Proporcionar estructuras de datos flexibles (DataFrames y Series).

- Simplificar el manejo de datos faltantes y diferentes tipos de datos.

##### 1.2.2 beneficios:

- Eficiencia: Operaciones rápidas y eficientes sobre grandes conjuntos de datos.

- Integración: Se integra bien con otras bibliotecas de Python, como NumPy y Matplotlib.

- Funcionalidades: Amplias funciones para limpieza, transformación y visualización de datos.


### 2. Instalación:

#### 2.1 Requisitos previos:

#####  Mínimos:

- SO: Windows 7/8/10, macOS, Linux.

- CPU: Doble núcleo (Intel Core i3).

- RAM: 4 GB.

- Disco: 1 GB libre.

##### recomendados:

- SO: Última versión de Windows, macOS, Linux.

- CPU: Cuatro núcleos (Intel Core i5).

- RAM: 8 GB o más.

- Disco: 10 GB libre.


### 3. Estructura del Proyecto:

#### 3.1 Organización de carpetas y archivos:

>  mi_proyecto/

> data/ 

> notebooks/    

>  Scripts/     

>  requirements.txt  

> README.md          

>  main.py             


### 4. Buenas Prácticas:

   - Código Limpio: Importancia de mantener el código legible y mantenible.

   - Nombres Descriptivos: Usar nombres claros para funciones, variables y clases.

   - Pruebas Unitarias: Importancia de incluir pruebas y ejemplos de cómo escribirlas.
   


### 5. Reglas de Escritura:

####  5.1 Estilo de Código: 

- > Indentación: 

Utiliza 4 espacios para la indentación en lugar de tabulaciones. Esto mejora la legibilidad del código.

#####  5.1.2 Espacios alrededor de operadores: 
>   Coloca un espacio antes y después de los operadores (por ejemplo, `=`, `+`, `-`, etc.) para mejorar la claridad.
   
    python
    df['columna'] = df['columna1'] + df['columna2']

##### 5.1.3 Espacios después de comas: 

>Incluye un espacio después de cada coma en listas o al seleccionar columnas.

     python
     df[['columna1', 'columna2']]
   
##### 5.4 Líneas largas:
>Si una línea de código es demasiado larga, usa paréntesis para dividirla en varias líneas.

    python
    resultado = (df[df['columna'] > 10]
                 .groupby('categoria')
                 .mean())
   

#####  5.1.5 Nombres descriptivos:

- Usa nombres claros y descriptivos para variables y DataFrames, evitando          abreviaciones innecesarias.

### 5.2 Convenciones de Nombres:

#####  Variables: 
> Usa `snake_case` para los nombres de DataFrames, describiendo su contenido.

       python
       ventas_totales = pd.DataFrame(data)

#####  Funciones:

> Si creas funciones que interactúan con DataFrames, mantén el `snake_case`    para que sean coherentes  con el estilo de Pandas.

      python
       def filtrar_ventas(df):
       return df[df['ventas'] > 100]

### 6. Modularización:

#### 6.1 Principios de Modularización: (Ventajas de dividir el código en módulos).

##### 6.1.1 Ejemplos:

    python
      Módulo: operaciones.py
     
     def sumar(a, b):
           Devuelve la suma de a y b.
         return a + b

     def restar(a, b):
            Devuelve la resta de a y b.
         return a - b

     python
       Módulo principal: main.py
     
     from operaciones import sumar, restar

     resultado_suma = sumar(5, 3)
     resultado_resta = restar(10, 4)

     print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")
     
