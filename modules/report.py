import streamlit as st
from datetime import datetime
import random
from firebase_admin import firestore  

db = firestore.client()

def fecha():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generar_numero_reporte(tipo_reporte):
    reportes_ref = db.collection(tipo_reporte)
    while True:
        numero_reporte = random.randint(1000, 9999)
        query = reportes_ref.where('numero_de_reporte', '==', numero_reporte).get()  # Cambia el nombre del campo
        if not query:
            return numero_reporte

def guardar_reporte(datos, tipo_reporte):
    try:
        db.collection(tipo_reporte).add(datos)
        st.success(f'Reporte de {tipo_reporte} guardado correctamente')
    except Exception as e:
        st.error(f'Error al guardar el reporte: {e}')

def campos_comunes():
    col1, col2 = st.columns(2)
    with col1:
        fecha_averia = st.date_input('Fecha de la averia :red[*]')
    with col2:
        hora_averia = st.time_input('Hora de la averia :red[*]')
    
    ciudad = st.selectbox('Ciudad de la Averia :red[*]', ['Seleccione una ciudad...', 'Barcelona', 'Puerto la Cruz'])
    direccion = st.text_input('Direccion de la Averia :red[*]')
    prioridad = st.select_slider('Prioridad del Reporte :red[*]', ['Baja', 'Media', 'Alta', 'Urgente'])
    descripcion = st.text_area('Descripcion detallada de la averia :red[*]')
    
    return fecha_averia, hora_averia, ciudad, direccion, prioridad, descripcion

def validar_datos(tipo_averia, descripcion, ciudad, direccion):
    if tipo_averia == 'Seleccione...':
        st.error('Debe seleccionar un tipo de averia')
        return False
    if not descripcion:
        st.error('Debe ingresar una descripcion para la averia')
        return False
    if ciudad == 'Seleccione una ciudad...':
        st.error('Debe elegir una ciudad para el reporte')
        return False
    if not direccion:
        st.error('Debe ingresar la direccion de la averia')
        return False
    return True

def generar_reporte(tipo_reporte, opciones_averia):
    fecha_hora = fecha()
    st.title(f'Reporte de {tipo_reporte}')
    
    numero_reporte = generar_numero_reporte(tipo_reporte)
    
    tipo_de_averia = st.selectbox(f'Seleccione el tipo de averia :red[*]', opciones_averia, index=0)
    fecha_averia, hora_averia, ciudad, direccion, prioridad, descripcion = campos_comunes()
    
    if st.button('Enviar Reporte'):
        if validar_datos(tipo_de_averia, descripcion, ciudad, direccion):
            datos = {
                'numero_de_reporte': numero_reporte,  # Cambia el nombre del campo
                'fecha_del_reporte': fecha_hora,
                'tipo_de_averia': tipo_de_averia,
                'fecha_de_la_averia': str(fecha_averia),
                'hora_de_la_averia': str(hora_averia),
                'ciudad': ciudad,
                'direccion': direccion,
                'prioridad_del_reporte': prioridad,
                'descripcion': descripcion
            }
            guardar_reporte(datos, tipo_reporte)
            mostrar_resumen(datos)

def mostrar_resumen(datos):
    st.success('Reporte enviado correctamente')
    st.write(f':blue[Hora y Fecha del reporte:] {datos["fecha_del_reporte"]}')  # Cambia el nombre del campo
    st.write(f':blue[Numero de Reporte:] {datos["numero_de_reporte"]}')  # Cambia el nombre del campo
    st.write(f':blue[Tipo de avería:] {datos["tipo_de_averia"]}')
    st.write(f':blue[Fecha y hora de la avería:] {datos["fecha_de_la_averia"]} {datos["hora_de_la_averia"]}')
    st.write(f':blue[Prioridad del reporte:] {datos["prioridad_del_reporte"]}')
    st.write(f':blue[Direccion del Reporte:] {datos["ciudad"]}, {datos["direccion"]}')
    st.write(f':blue[Descripción:] {datos["descripcion"] if datos["descripcion"] else "No proporcionada"}')

def menu():
    fecha_hora = fecha()
    menu = ['Reportes de Agua', 'Reportes de Salud', 'Reportes de Electricidad', 'Reportes de Vialidad', 'Reportes de Educacion', 'Reportes de Comunicacion', 'Reportes de Transpote', 'Reportes de Seguridad', 'Reportes de Saneamiento', "Calendario de Reportes"]  # Eliminé la opción "Ver Reportes", (Angel: Añadí la opción ver calendario)
    st.sidebar.title(':blue-background[Menu de Reportes]')
    choice = st.sidebar.selectbox('Seleccione una opción', menu, index=0)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Servicio de Reportes')
    with col3:
        st.write(fecha_hora)
    
    if choice == 'Reportes de Agua':
        generar_reporte('Agua', ['Seleccione...','Rotura de Tuberias', 'Falta de suministro' ,'Baja Presion', 'Agua Turbia', 'Contaminacion del Agua', 'Problemas de Cloracion', 'Problemas de Olor', 'Sistema de Drenaje', 'Reparacion de Alcantarillas', 'Taponamientos'])
    
    elif choice == 'Reportes de Salud':
        generar_reporte('Salud', ['Seleccione...','Falta de Medicamentos', 'Falta de Personal Medico' ,'Equipos Medicos Averiados', 'Falta de Suministros Medicos', 'Retrasos en Atencion', 'Problemas de Saneamiento', 'Condiciones Insalubres', 'Interrupcion del Servicio', 'Problemas de Infraestructura', 'Problemas en Laboratorios', 'Cortes de Energia', 'Falta de Agua', 'Problemas en el Sistema de Gestión de Pacientes'])
        
    elif choice == 'Reportes de Electricidad':
        generar_reporte('Electricidad', ['Seleccione...','Apagon', 'Interrupciones Intermitentes' ,'Baja Tension', 'Sobrecargas', 'Caida de Poste', 'Caida de Cableado', 'Caida de Transformador', 'Averias en el Alumbrado Publico'])
        
    elif choice == 'Reportes de Vialidad':
        generar_reporte('Vialidad', ['Seleccione...','Baches', 'Semaforos Averiados', 'Accidentes Viales', 'Obstruccion de Vias', 'Señalizacion Dañada', "Daños en puentes", "Daños en Paso Peatonales", "Falta de Pasos Peatonales"])
        
    elif choice == 'Reportes de Educacion':
        generar_reporte('Educacion', ['Seleccione...', "Falta de Personal Docente", "Infraestructura Dañada", "Falta de Materiales Educativos", "Problemas de Saneamiento", "Cortes de Energia", "Falta de Agua", "Problemas de Transporte Escolar", "Problemas de Seguridad", "Falta de Mobiliario"])
        
    elif choice == 'Reportes de Comunicacion':
        generar_reporte('Comunicacion', ['Seleccione...', "Cortes de Internet", "Problemas de Telefonia", "Falta de Señal de Television", "Averias en Redes de Comunicacion", "Problemas de Radio", "Falta de Equipos de Comunicacion", "Interrupciones en Servicio"])
        
    elif choice == 'Reportes de Transpote':
        generar_reporte('Transporte', ['Seleccione...', "Retrasos en Rutas", "Falta de Unidades", "Problemas de Seguridad", "Averias en Vehiculos", "Falta de Personal", "Problemas de Limpieza", "Problemas de Tarifa", "Problemas de Accesibilidad"])
        
    elif choice == 'Reportes de Seguridad':
        generar_reporte('Seguridad', ['Seleccione...', "Robos", "Asaltos", "Amenazas", "Problemas de Violencia",  "Problemas de Drogas", "Problemas de Alcoholismo", "Problemas de Pandillas", "Problemas de Prostitucion", "Problemas de Vandalismo", "Problemas de Discriminacion", "Problemas de Acoso", "Problemas en Centro de Detencion", "Incendios", "Emergencias Medicas"])
        
    elif choice == 'Reportes de Saneamiento':
        generar_reporte("Seguridad", ["Seleccione...", "Falta de Recoleccion de Basura", "Contenedores Llenos", "Residuos en la Via Publica", "Problemas de Reciclaje", "Vertederos Ilegales", "Problemas con Camiones de Basura", "Malos Olores", "Problemas de Limpieza en Espacios Publicos"])
        #(Jhuliana: Añadi nuevas opciones de reportes)
    
    elif choice == 'Calendario de Reportes':
        from modules.Calendario import mostrar_calendario
        mostrar_calendario() # Añadidura de la muestra del calendario