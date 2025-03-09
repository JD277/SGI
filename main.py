import streamlit as st
import pandas as pd
from modules.database.dbmanager import DbManager
st.set_page_config(page_title='Gestion de Servicios Publicos', layout='centered', initial_sidebar_state='collapsed')

@st.cache_resource
def get_db_manager():
    return DbManager(
        'modules/database/estructuras.json',
        'https://estructuras-9be66-default-rtdb.firebaseio.com/'
    )

db_manager = get_db_manager()
@st.cache_resource
def get_all():
    reportes_lista = db_manager.read_record() 
    reportes_final = []
    for reporte in reportes_lista:
            reportes_final.append(reportes_lista[reporte])

    df = pd.DataFrame(reportes_final)
        
    df['date_of_failure'] = pd.to_datetime(df['date_of_failure'])
    df['date_of_record'] = pd.to_datetime(df['date_of_record'])
    return df
df = get_all()
if 'user_type' not in st.session_state:
    st.session_state.user_type = None  # Estado del usuario (admin o None)

def main():
    global state
    if st.session_state.user_type == 'admin':
        menu = ['Inicio', 'Objetivo', 'Reportar', 'Buscar reporte', 'Panel de Reportes', 'Metricas y Resultados', 'Calendario de reportes','Cerrar sesión','Registrar Administrador']
        icons = {
            "Inicio": ":material/house:",
            "Objetivo": ":material/emoji_objects:",
            "Reportar": ":material/report:",
            "Buscar reporte": ":material/search:",
            "Panel de Reportes": ":material/browse_activity:",
            "Metricas y Resultados": ":material/trending_up:",
            "Calendario de reportes": ":material/calendar_month:",
            "Cerrar sesión": ":material/logout:",
            "Registrar Administrador": ":material/account_circle:"
        }
    else:
        menu = ['Inicio', 'Objetivo', 'Reportar', 'Buscar reporte','Iniciar sesión']
        icons = {
            "Inicio": ":material/house:",
            "Objetivo": ":material/emoji_objects:",
            "Reportar": ":material/report:",
            "Buscar reporte": ":material/search:",
            "Iniciar sesión": ":material/account_circle:"
        }
    st.sidebar.title(':material/menu: Menu de seleccion')
    choice = st.sidebar.radio('Seleccione una opcion', [f"{icons[item]} {item}" for item in menu])

    if choice.startswith(":material/house:"):
        import modules.inicio as inicio
        inicio.inicio()

    elif choice.startswith(":material/emoji_objects:"):
        import modules.objetivo as objetivo
        objetivo.obj()

    elif choice.startswith(":material/report:"):
        from modules.report import Report_screen
        report = Report_screen(db_manager)
        report.menu()

    elif choice.startswith(":material/search:"):
        from modules.monitoreo import Monitor_screen
        monitoreo = Monitor_screen(db_manager)
        monitoreo.menu()

    elif choice.startswith(":material/browse_activity:"):
        from modules.tablas import Tables
        tablas = Tables(df)
        tablas.main()
    
    elif choice.startswith(":material/trending_up:"):
        from modules.metricas import Statics
        metricas = Statics(df)
        metricas.menu() 

    elif choice.startswith(":material/calendar_month:"):
        from modules.Calendario import Calendar_screen
        calendario = Calendar_screen(db_manager)
        calendario.show()

    elif choice.startswith(":material/account_circle:"):
        from modules.database.auth import Auth
        auth = Auth()
        if st.session_state.user_type != 'admin':
            auth.admin_ui('Iniciar sesión')
        else:
            auth.admin_ui('Registrar')

    elif choice.startswith(":material/logout:"):
        st.session_state.user_type = None  # Cerrar sesión
        st.rerun()  # Recargar la página
        
if __name__ == '__main__':
    main()
