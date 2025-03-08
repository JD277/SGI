import streamlit as st
from datetime import datetime
from streamlit_calendar import calendar

def obtener_reportes():
    """Obtiene todos los reportes de Firestore"""
    tipos_reporte = ['Agua', 'Salud', 'Electricidad']
    todos_reportes = []
    
    for tipo in tipos_reporte:
        reportes_ref = db.collection(tipo).stream()
        for reporte in reportes_ref:
            datos = reporte.to_dict()
            datos['tipo_reporte'] = tipo  # Añade el tipo de reporte
            todos_reportes.append(datos)
    
    return todos_reportes

def generar_eventos(reportes):
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
            fecha_str = reporte['fecha_de_la_averia']
            hora_str = reporte['hora_de_la_averia'].split('.')[0]  # Remueve microsegundos si existen
            fecha_hora = datetime.strptime(f"{fecha_str} {hora_str}", "%Y-%m-%d %H:%M:%S")
            
            eventos.append({
                'title': f"{reporte['tipo_de_averia']} ({reporte['tipo_reporte']})",
                'start': fecha_hora.isoformat(),
                'color': colores.get(reporte['tipo_reporte'], '#CCCCCC'),
                'allDay': False,
                'extendedProps': {
                    'prioridad': reporte['prioridad_del_reporte'],
                    'descripcion': reporte['descripcion']
                }
            })
        except Exception as e:
            st.error(f"Error procesando reporte: {e}")
    return eventos

def mostrar_calendario():
    """Muestra el calendario interactivo con Streamlit"""
    st.title("🗓️ Calendario de Reportes")
    
    # Obtiene y procesa datos
    reportes = db_manager.read_records()
    eventos = generar_eventos(reportes)
    
    # Configura el calendario
    opciones_calendario = {
        'headerToolbar': {
            'left': 'today prev,next',
            'center': 'title',
            'right': 'dayGridMonth,timeGridWeek,timeGridDay listWeek'
        },
        'initialView': 'dayGridMonth',
        'eventClick': "(event) => {alert(event.event.extendedProps.descripcion);}"
    }
    
    # Muestra el calendario
    calendario_seleccionado = calendar(
        events=eventos,
        options=opciones_calendario,
        key="report_calendar"
    )
    
    # Muestra los detalles al hacer clic en evento
    if calendario_seleccionado.get('eventClick'):
        evento = calendario_seleccionado['eventClick']['event']
        with st.expander("Detalles del Reporte"):
            st.markdown(f"""
            **Tipo de avería:** {evento['title']}  
            **Prioridad:** {evento['extendedProps']['prioridad']}  
            **Descripción:** {evento['extendedProps']['descripcion']}
            """) # Listo