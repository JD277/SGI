import streamlit as st
import random
from firebase_admin import firestore
from pdf import *


db = firestore.client()

def buscar_reporte(tipo_reporte, numero_reporte):
    reportes_ref = db.collection(tipo_reporte)
    query = reportes_ref.where('numero_de_reporte', '==', numero_reporte).get()
    
    if query:
        reporte = query[0].to_dict()
        return reporte
    return None

def mostrar_reporte(reporte):
    st.success('Reporte encontrado:')
    st.write(f":blue[Número de Reporte:] {reporte['numero_de_reporte']}")
    st.write(f":blue[Fecha del Reporte:] {reporte['fecha_del_reporte']}")
    st.write(f":blue[Tipo de Avería:] {reporte['tipo_de_averia']}")
    st.write(f":blue[Fecha de la Avería:] {reporte['fecha_de_la_averia']}")
    st.write(f":blue[Hora de la Avería:] {reporte['hora_de_la_averia']}")
    st.write(f":blue[Ciudad:] {reporte['ciudad']}")
    st.write(f":blue[Dirección:] {reporte['direccion']}")
    st.write(f":blue[Prioridad del Reporte:] {reporte['prioridad_del_reporte']}")
    st.write(f":blue[Descripción:] {reporte['descripcion']}")

def crearTextPDF(reporte):
    body= "Numero de Reporte: " + {reporte['numero_de_reporte']} 
    return body      

def menu():
    st.title('Buscar Reporte por Número')
    
    tipo_reporte = st.selectbox(
        'Seleccione el tipo de reporte:',
        ['Agua', 'Salud', 'Electricidad']
    )
    
    numero_reporte = st.number_input(
        'Ingrese el número de reporte:',
        min_value=1,
        step=1
    )
    
    if st.button('Buscar Reporte'):
        reporte = buscar_reporte(tipo_reporte, numero_reporte)
        if reporte is not None:
            mostrar_reporte(reporte)
        else:
            st.error('No se encontró ningún reporte con ese número.')

    if st.button("Generar PDF"):
        reporte = buscar_reporte(tipo_reporte, numero_reporte)
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
