import streamlit as st
from datetime import datetime
from streamlit_calendar import calendar
import time
from modules.database.dbmanager import DbManager

class Calendar_screen():
    def __init__(self, db_manager:DbManager):
        self.db_manager = db_manager

    def get_records(self):
        """Obtiene todos los reportes de Firestore"""
        ids = self.db_manager.read_record()
        all = []
        for id in ids:
            report = ids[id]
            if type(report['date_of_failure']) == int:
               report['date_of_failure'] = self.unix_to_string_time(report['date_of_failure'])
            if type(report['date_of_record']) == int:
               report['date_of_record'] = self.unix_to_string_time(report['date_of_record'])
            all.append(report)
        return all

    def generate_events(self, reportes):
        """Convierte los reportes en eventos para el calendario"""
        colores = {
            'Agua': '#4285F4',    # Azul
            'Salud': '#EA4335',   # Rojo
            'Electricidad': '#FBBC05' # Amarillo
        }
        
        eventos = []
        for reporte in reportes:
            try:
                # Combina la fecha y hora del reporte
                fecha_str = reporte['date_of_failure']
                
                eventos.append({
                    'title': f"{reporte['service']} ({reporte['city']})",
                    'start': fecha_str,
                    'color': colores.get(reporte['service'], '#CCCCCC'),
                    'allDay': False,
                    'extendedProps': {
                        'prioridad': reporte['priority'],
                        'descripcion': reporte['description']
                    }
                })
            except Exception as e:
                st.error(f"Error procesando reporte: {e}")
        return eventos
    def unix_to_string_time(self,ts):
        try:
            return time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.gmtime(ts)  # UTC
            )
        except Exception as e:
            return f"Error: {e}"
    def show(self,):
        """Muestra el calendario interactivo con Streamlit"""
        st.title("🗓️ Calendario de Reportes")
        
        # Obtiene y procesa datos
        reportes = self.get_records()
        eventos = self.generate_events(reportes)
        
        # Configura el calendario (eliminamos el eventClick de las opciones)
        opciones_calendario = {
             'headerToolbar': {
                 'left': 'today prev,next',
                 'center': 'title',
                 'right': 'dayGridMonth,timeGridWeek,timeGridDay listWeek'
             },
             'initialView': 'dayGridMonth'
        }
        
        # Muestra el calendario y captura eventos
        calendario_seleccionado = calendar(
             events=eventos,
             options=opciones_calendario,
             key="report_calendar"
        )
        
        # Manejo de clic en evento
        if calendario_seleccionado.get('eventClick'):
            evento = calendario_seleccionado['eventClick']['event']
            with st.expander("Detalles del Reporte", expanded=True):
                st.markdown(f"""
                **Tipo de avería:** {evento['title']}  
                **Prioridad:** {evento['extendedProps']['prioridad']}  
                **Descripción:** {evento['extendedProps']['descripcion']}
                """)