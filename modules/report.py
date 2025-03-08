import streamlit as st
from datetime import datetime

class Report_screen:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        
    def fecha(self, ):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def report(self, datos):

        try:
            self.db_manager.write_record(datos)
            st.success(f"Reporte de {datos['service']} guardado correctamente")
        except Exception as e:
            st.error(f'Error al guardar el reporte: {e}')
        self.mostrar_resumen(datos)

    def campos_comunes(self):
        col1, col2 = st.columns(2)
        with col1:
            fecha_averia = st.date_input('Fecha de la averia :red[*]')
        with col2:
            hora_averia = st.time_input('Hora de la averia :red[*]')
        
        ciudad = st.selectbox('Ciudad de la Averia :red[*]', ['Seleccione una ciudad...', 'Barcelona', 'Puerto la Cruz'])
        direccion = st.text_input('Direccion de la Averia :red[*]')
        descripcion = st.text_area('Descripcion detallada de la averia :red[*]')
        
        return fecha_averia, hora_averia, ciudad, direccion, descripcion

    def validate_data(self, tipo_averia, descripcion, ciudad, direccion):
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

    def  make_report(self, tipo_reporte, opciones_averia):
        fecha_hora = self.fecha()
        st.title(f'Reporte de {tipo_reporte}')
        
        
        tipo_de_averia = st.selectbox(f'Seleccione el tipo de averia :red[*]', opciones_averia, index=0)
        fecha_averia, hora_averia, ciudad, direccion, descripcion = self.campos_comunes()
        descripcion = '| Tipo de averia: ' + tipo_de_averia + ' | Descripción: ' + descripcion
        if st.button('Enviar Reporte'):
            prioridad = "low"
            days = (fecha_averia - datetime.now().date()).days
            high_keywords = ['urgente', 'emergencia', 'critico', 'inmediato']
            medium_keywords = ['importante', 'prioritario', 'necesario']
            for word in high_keywords:
                if word in descripcion.lower() or days > 50:
                    prioridad = 'high'
                    if self.validate_data(tipo_de_averia, descripcion, ciudad, direccion):
                        datos = {
                                "city": ciudad,
                                "date_of_record": fecha_hora,
                                "date_of_failure": fecha_averia.strftime("%Y-%m-%d %H:%M:%S"),
                                "description": descripcion,
                                "service": tipo_reporte,
                                "street": direccion,
                                "priority": prioridad
                            }
                        self.report(datos)
                        return

            for word in medium_keywords:
                if word in descripcion.lower() or days > 30:
                    prioridad = 'medium'
                    if self.validate_data(tipo_de_averia, descripcion, ciudad, direccion):
                        datos = {
                                "city": ciudad,
                                "date_of_record": fecha_hora,
                                "date_of_failure": fecha_averia.strftime("%Y-%m-%d %H:%M:%S"),
                                "description": descripcion,
                                "service": tipo_reporte,
                                "street": direccion,
                                "priority": prioridad
                            }
                        self.report(datos)                    
                        break
  




    def mostrar_resumen(self, datos):
        st.success('Reporte enviado correctamente')
        st.write(f':blue[Hora y Fecha del reporte:] {datos["date_of_record"]}')  # Cambia el nombre del campo
        st.write(f':blue[Tipo de avería:] {datos["service"]}')
        st.write(f':blue[Fecha y hora de la avería:] {datos["date_of_failure"]}')
        st.write(f':blue[Prioridad del reporte:] {datos["priority"]}')
        st.write(f':blue[Direccion del Reporte:] {datos["city"]}, {datos["street"]}')
        st.write(f':blue[Descripción:] {datos["description"] if datos["description"] else "No proporcionada"}')

    def menu(self):
        fecha_hora = self.fecha()
        menu = ['Reportes de Agua', 'Reportes de Salud', 'Reportes de Electricidad', 'Reportes de Vialidad', 'Reportes de Educacion', 'Reportes de Comunicacion', 'Reportes de Transpote', 'Reportes de Seguridad', 'Reportes de Saneamiento', "Calendario de Reportes"]  # Eliminé la opción "Ver Reportes", (Angel: Añadí la opción ver calendario)
        st.sidebar.title(':blue-background[Menu de Reportes]')
        choice = st.sidebar.selectbox('Seleccione una opción', menu, index=0)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('Servicio de Reportes')
        with col3:
            st.write(fecha_hora)
        
        if choice == 'Reportes de Agua':
            self.make_report('Agua', ['Seleccione...','Rotura de Tuberias', 'Falta de suministro' ,'Baja Presion', 'Agua Turbia', 'Contaminacion del Agua', 'Problemas de Cloracion', 'Problemas de Olor', 'Sistema de Drenaje', 'Reparacion de Alcantarillas', 'Taponamientos'])
        
        elif choice == 'Reportes de Salud':
            self.make_report('Salud', ['Seleccione...','Falta de Medicamentos', 'Falta de Personal Medico' ,'Equipos Medicos Averiados', 'Falta de Suministros Medicos', 'Retrasos en Atencion', 'Problemas de Saneamiento', 'Condiciones Insalubres', 'Interrupcion del Servicio', 'Problemas de Infraestructura', 'Problemas en Laboratorios', 'Cortes de Energia', 'Falta de Agua', 'Problemas en el Sistema de Gestión de Pacientes'])
            
        elif choice == 'Reportes de Electricidad':
            self.make_report('Electricidad', ['Seleccione...','Apagon', 'Interrupciones Intermitentes' ,'Baja Tension', 'Sobrecargas', 'Caida de Poste', 'Caida de Cableado', 'Caida de Transformador', 'Averias en el Alumbrado Publico'])
            
        elif choice == 'Reportes de Vialidad':
            self.make_report('Vialidad', ['Seleccione...','Baches', 'Semaforos Averiados', 'Accidentes Viales', 'Obstruccion de Vias', 'Señalizacion Dañada', "Daños en puentes", "Daños en Paso Peatonales", "Falta de Pasos Peatonales"])
            
        elif choice == 'Reportes de Educacion':
            self.make_report('Educacion', ['Seleccione...', "Falta de Personal Docente", "Infraestructura Dañada", "Falta de Materiales Educativos", "Problemas de Saneamiento", "Cortes de Energia", "Falta de Agua", "Problemas de Transporte Escolar", "Problemas de Seguridad", "Falta de Mobiliario"])
            
        elif choice == 'Reportes de Comunicacion':
            self.make_report('Comunicacion', ['Seleccione...', "Cortes de Internet", "Problemas de Telefonia", "Falta de Señal de Television", "Averias en Redes de Comunicacion", "Problemas de Radio", "Falta de Equipos de Comunicacion", "Interrupciones en Servicio"])
            
        elif choice == 'Reportes de Transpote':
            self.make_report('Transporte', ['Seleccione...', "Retrasos en Rutas", "Falta de Unidades", "Problemas de Seguridad", "Averias en Vehiculos", "Falta de Personal", "Problemas de Limpieza", "Problemas de Tarifa", "Problemas de Accesibilidad"])
            
        elif choice == 'Reportes de Seguridad':
            self.make_report('Seguridad', ['Seleccione...', "Robos", "Asaltos", "Amenazas", "Problemas de Violencia",  "Problemas de Drogas", "Problemas de Alcoholismo", "Problemas de Pandillas", "Problemas de Prostitucion", "Problemas de Vandalismo", "Problemas de Discriminacion", "Problemas de Acoso", "Problemas en Centro de Detencion", "Incendios", "Emergencias Medicas"])
            
        elif choice == 'Reportes de Saneamiento':
            self.make_report("Saneamiento", ["Seleccione...", "Falta de Recoleccion de Basura", "Contenedores Llenos", "Residuos en la Via Publica", "Problemas de Reciclaje", "Vertederos Ilegales", "Problemas con Camiones de Basura", "Malos Olores", "Problemas de Limpieza en Espacios Publicos"])
        