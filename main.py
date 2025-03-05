import streamlit as st
import firebase_admin
from firebase_admin import credentials
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase_config.json')  
    firebase_admin.initialize_app(cred)
import modules.inicio as inicio
import modules.objetivo as objetivo
import modules.report as report
import modules.monitoreo as monitoreo
import modules.tablas as tablas
import modules.metricas as metricas

st.set_page_config(page_title='Gestion de Servicios Publicos', layout='centered', initial_sidebar_state='collapsed')

def main():
    menu = ['Inicio', 'Objetivo', 'Reportes', 'Monitoreo', 'Panel de Reportes', 'Metricas y Resultados']
    icons = {
        "Inicio": ":material/house:",
        "Objetivo": ":material/emoji_objects:",
        "Reportes": ":material/report:",
        "Monitoreo": ":material/monitoring:",
        "Panel de Reportes": ":material/browse_activity:",
        "Metricas y Resultados": ":material/trending_up:"
    }

    st.sidebar.title(':blue-background[Menu de seleccion]')
    choice = st.sidebar.radio('Seleccione una opcion', [f"{icons[item]} {item}" for item in menu])

    if choice.startswith(":material/house:"):
        inicio.inicio()

    elif choice.startswith(":material/emoji_objects:"):
        objetivo.obj()

    elif choice.startswith(":material/report:"):
        report.menu()

    elif choice.startswith(":material/monitoring:"):
        monitoreo.menu()

    elif choice.startswith(":material/browse_activity:"):
        tablas.main()
    
    elif choice.startswith(":material/trending_up:"):
        metricas.menu() 
        
if __name__ == '__main__':
    main()