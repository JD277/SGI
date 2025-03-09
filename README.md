# SGI
<div style="text-align: center;">
    <img src="images/logopdf.png" alt="Logo del proyecto" style="max-width: 30%; height: auto; border: 2px solid #ccc; border-radius: 10px;">
</div>

## Descripción del Proyecto

SGI es una plataforma la cual gestiona y administra reportes relacionados con servicios publicos como pueden ser la electricidad, el agua y la salud, esto mediante el llenado de formularios los cuales son clasificados por prioridad, buscando optimizar el monitoreo de las incidencias, para que sean solucionadas de forma rápida y eficiente.

Este sistema se encuentra basado en la implementación de una base de datos alojada en la nube (mediante el uso de Firebase) para almacenar toda la información de los distintos formularios que contienen la información de los reportes de averías, en conjunto con Python para llevar a cabo la implementación del código.

## Funcionalidades del Sistema

### 1. Generación de reportes

### 2. Mostrado de gráficos de reportes, organizados por:
- Ciudad.
- Tipo de averia.
- Evolución temporal.

### 3. Control de reportes basado en su prioridad.

## Instalación y Uso

### Requisitos Previos
- Python 3.9 o superior

## Tecnologías Utilizadas
- **Python**
- **Firebase** (Base de datos)
- **Pandas** (Análisis de datos)
- **Pillow** (Manejo de imágenes)
- **Matplotlib** (Visualización de gráficos)

## Instrucciones de Uso

1. Clona el repositorio en tu computadora:
   ```bash
   git clone https://github.com/JD277/SGI.git
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install firebase-admin Pillow pandas matplotlib
   ```
3. Ejecuta el programa principal:
   ```bash
   python App.py
   ```

## Cómo Subir Cambios al Proyecto en GitHub

### Haciendo Commits mediante la Web de GitHub
1. Ve al repositorio del proyecto en GitHub.
2. Dirígete al archivo que deseas modificar y haz clic en el ícono de edición (lápiz).
3. Realiza los cambios necesarios en el archivo.
4. Escribe un mensaje de commit claro en el campo "Commit changes".
5. Selecciona "Commit directly to the main branch" si los cambios no requieren revisión, o crea un nuevo branch y un Pull Request.
6. Haz clic en "Commit changes".

## Convenciones para Commits
Cada colaborador debe trabajar en su módulo correspondiente y hacer commits siguiendo la estructura:

- **Nuevo cambio:** `Feat(feature): description`
- **Refactorización:** `Refactor(feature): description`
- **Eliminación:** `Delete(feature): description`
- **Pull Request:** `Merge(feature): description`

## Contacto
Si tienes dudas o sugerencias, abre un issue en el repositorio o contacta al equipo vía GitHub.
