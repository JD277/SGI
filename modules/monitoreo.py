import streamlit as st
from modules.PDF.pdf import *
from modules.database.dbmanager import DbManager

class Monitor_screen():
    def __init__(self, db_manager:DbManager):
        self.db_manager = db_manager
    def buscar(self,num):
        result = self.db_manager.get_report_by_id(num)
        return result
    
    def mostrar_reporte(self,reporte):
        st.success('Reporte encontrado:')
        record = unix_to_string_time(ts=reporte['date_of_record'])
        failure = unix_to_string_time(ts=reporte['date_of_failure'])
        st.write(f":blue[Fecha del Reporte:] {record}")
        st.write(f":blue[Fecha de la Avería:] {failure}")
        st.write(f":blue[Ciudad:] {reporte['city']}")
        st.write(f":blue[Dirección:] {reporte['street']}")
        st.write(f":blue[Prioridad del Reporte:] {reporte['priority']}")
        st.write(f":blue[Descripción:] {reporte['description']}")

    def menu(self):
        st.title('Buscar Reporte por Número')
        
        numero_reporte = st.text_input('Ingrese el número de reporte:', key="numero_reporte")
        
        if st.button('Buscar Reporte'):
            reporte = self.buscar(numero_reporte)
            if reporte is not None:
                self.mostrar_reporte(reporte)
            else:
                st.error('No se encontró ningún reporte con ese número.')

        if st.button("Generar PDF"):
            reporte = self.buscar(numero_reporte)
            if reporte is not None:
                texto = contenido(reporte, numero_reporte)
                crear_pdf(texto)
            with open("reporte.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(
                label="Descargar PDF",
                data=PDFbyte,
                file_name="reporte.pdf",
                mime='application/octet-stream'
            )
