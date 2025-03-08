import streamlit as st
from fpdf import FPDF

def contenido(reporte):
    st.success('Se ha generado un PDF:')
    num_reporte =  f"Numero de reporte: {reporte['numero_de_reporte']}"
    fecha_reporte =  f"fecha del reporte: {reporte['fecha_del_reporte']}"
    tipo_averia=  f"tipo de averia: {reporte['tipo_de_averia']}"
    fecha_averia =  f"fecha de averia: {reporte['fecha_de_la_averia']}"
    hora_averia =  f"hora de averia: {reporte['hora_de_la_averia']}"
    ciudad =  f"ciudad: {reporte['ciudad']}"
    direccion = f"Direccion: {reporte['direccion']}"
    prioridad =  f"Prioridad del reporte: {reporte['prioridad_del_reporte']}"
    descripcion =  f"Descripcion: {reporte['descripcion']}"

    texto = f"DATOS DEL REPORTE:\n\n{num_reporte}\n{fecha_reporte}\n{tipo_averia}\n{fecha_averia}\n{hora_averia}\n{ciudad}\n{direccion}\n{prioridad}\n{descripcion}"
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
    


