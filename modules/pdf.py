import streamlit as st
from fpdf import FPDF
from firebase_admin import firestore

db = firestore.client()
    
def contenido(reporte):
    st.success('Se ha generado un PDF:')
    num =  f"Numero de roporte: {reporte['numero_de_reporte']}"
    fechaRep =  f"fecha del reporte: {reporte['fecha_del_reporte']}"
    tipoAveria=  f"tipo de averia: {reporte['tipo_de_averia']}"
    fechaAveria =  f"fecha de averia: {reporte['fecha_de_la_averia']}"
    horaAveria =  f"hora de averia: {reporte['hora_de_la_averia']}"
    ciudad =  f"ciudad: {reporte['ciudad']}"
    direccion = f"Direccion: {reporte['direccion']}"
    prioridad =  f"Prioridad del reporte: {reporte['prioridad_del_reporte']}"
    descripcion =  f"Descripcion: {reporte['descripcion']}"

    texto = f"DATOS DEL REPORTE:\n\n{num}\n{fechaRep}\n{tipoAveria}\n{fechaAveria}\n{horaAveria}\n{ciudad}\n{direccion}\n{prioridad}\n{descripcion}"
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
    pdf.logo("logopdf.png", 80,0,0,50)
    pdf.titles("Reporte de servicio publico")
    pdf.output("reporte.pdf", 'F')
    


