import streamlit as st
from fpdf import FPDF
import time
def unix_to_string_time(ts):
        try:
            return time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.gmtime(ts)  # UTC
            )
        except Exception as e:
            return f"Error: {e}"
def contenido(report,id):
    st.success('Se ha generado un PDF:')
    num_reporte =  f"Numero de reporte: {id}"
    fecha_reporte = 0
    fecha_averia = 0
    if type(report['date_of_failure']) == int:
        report['date_of_failure'] = unix_to_string_time(report['date_of_failure'])
        fecha_averia =  f"fecha de averia: {report['date_of_failure']}"
    else:
        fecha_averia =  f"fecha de averia: {report['date_of_failure']}"

    if type(report['date_of_record']) == int:
        report['date_of_record'] = unix_to_string_time(report['date_of_record'])
        fecha_reporte =  f"fecha del reporte: {report['date_of_record']}"
    else:
        fecha_reporte =  f"fecha del reporte: {report['date_of_record']}"

    tipo_averia=  f"Servicio: {report['service']}"
    ciudad =  f"ciudad: {report['city']}"
    direccion = f"Direccion: {report['street']}"
    prioridad =  f"Prioridad del reporte: {report['priority']}"
    descripcion =  f"Descripcion: {report['description']}"

    texto = f"DATOS DEL REPORTE:\n\n{num_reporte}\n{fecha_reporte}\n{tipo_averia}\n{fecha_averia}\n{ciudad}\n{direccion}\n{prioridad}\n{descripcion}"
    return texto

class PDF(FPDF):
    pass
    def logo(self, name, x, y ,w, h):
        self.image(name, x, y, w, h)

    def text(self, texto):
        self.set_xy(8, 70)
        self.set_text_color(0,0,0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, texto)

    def titles(self, title):
        self.set_xy(0,0)
        self.set_font('Arial', 'B', 20)
        self.set_text_color(0,0,0)
        self.cell(w=210.0,h=90.0, align='C', txt=title, border=0)


def crear_pdf(dato):
    pdf = PDF()
    pdf.add_page()
    pdf.text(dato)
    pdf.logo("images/logopdf.png", 80,0,0,50)
    pdf.titles("Reporte de servicio publico")
    pdf.output("reporte.pdf", 'F')
    


