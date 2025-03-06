import streamlit as st
import pandas as pd
from PIL import Image
from firebase_admin import firestore

db = firestore.client()

img1 = Image.open('images/img5.png')
img2 = Image.open('images/img6.png')
img3 = Image.open('images/img8.png')

def mostrar_reportes_como_tabla(tipo_reporte):
    reportes_ref = db.collection(tipo_reporte)
    reportes = reportes_ref.stream()
    
    reportes_lista = [reporte.to_dict() for reporte in reportes]
    
    if not reportes_lista:
        st.warning(f"No hay reportes registrados para {tipo_reporte}.")
        return
    
    df = pd.DataFrame(reportes_lista)
    
    st.write(f"Reportes de {tipo_reporte}:")
    st.dataframe(df)

def main():
    st.title('Panel de Reportes')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image(img1, width=800)
        bot1 = st.button('Mostrar', key = 'Agua')
    with col2:
        st.image(img2, width=800)
        bot2 = st.button('Mostrar', key = 'Electricidad')
    with col3:
        st.image(img3, width=700)
        bot3 = st.button('Mostrar', key = 'Salud')

    if bot1:
        mostrar_reportes_como_tabla('Agua')
    
    elif bot2:
        mostrar_reportes_como_tabla('Electricidad')
    
    elif bot3:
        mostrar_reportes_como_tabla('Salud')