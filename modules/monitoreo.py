import streamlit as st
import random
from firebase_admin import firestore
from modules.pdf import *
from modules.database.dbmanager import DbManager
from datetime import datetime

def buscar(num):
    global db_manager
    result = db_manager.get_report_by_id(num)
    return result

def mostrar_reporte(reporte):
    st.success('Reporte encontrado:')
    st.write(f":blue[Fecha del Reporte:] {reporte['date_of_record']}")
    st.write(f":blue[Fecha de la Avería:] {reporte['date_of_failure']}")
    st.write(f":blue[Ciudad:] {reporte['city']}")
    st.write(f":blue[Dirección:] {reporte['street']}")
    st.write(f":blue[Prioridad del Reporte:] {reporte['prioridad_del_reporte']}")
    st.write(f":blue[Descripción:] {reporte['description']}")

def crearTextPDF(reporte):
    body= "Numero de Reporte: " + {reporte['numero_de_reporte']} 
    return body      

def menu():
    db_manager = DbManager('modules/database/estructuras.json', 'https://estructuras-9be66-default-rtdb.firebaseio.com/',f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    st.title('Buscar Reporte por Número')
    
    tipo_reporte = st.selectbox(
        'Seleccione el tipo de reporte:',
        ['Agua', 'Salud', 'Electricidad']
    )
    
    numero_reporte = st.text_input('Ingrese el número de reporte:', key="numero_reporte")
    
    if st.button('Buscar Reporte'):
        reporte = buscar(numero_reporte)
        print(reporte)
        if reporte is not None:
            mostrar_reporte(reporte)
        else:
            st.error('No se encontró ningún reporte con ese número.')

    if st.button("Generar PDF"):
        reporte = buscar(numero_reporte)
        if reporte is not None:
            texto = contenido(reporte)
            crear_pdf(texto)
        with open("reporte.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label="Descargar PDF",
            data=PDFbyte,
            file_name="reporte.pdf",
            mime='application/octet-stream'
        )
