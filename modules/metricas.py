import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from firebase_admin import firestore

db = firestore.client()

def get_records(tipo_reporte):
    reportes_ref = db.collection(tipo_reporte)
    reportes = reportes_ref.stream()
    reportes_lista = [reporte.to_dict() for reporte in reportes]
    return pd.DataFrame(reportes_lista)

def grafico_reportes_por_ciudad(df):
    st.subheader("Reportes por Ciudad")
    reportes_por_ciudad = df['ciudad'].value_counts()
    st.bar_chart(reportes_por_ciudad)

def grafico_reportes_por_tipo_averia(df):
    st.subheader("Reportes por Tipo de Avería")
    reportes_por_tipo = df['tipo_de_averia'].value_counts()
    st.bar_chart(reportes_por_tipo)

def grafico_evolucion_temporal(df):
    st.subheader("Evolución de Reportes en el Tiempo")
    df['fecha_del_reporte'] = pd.to_datetime(df['fecha_del_reporte'])
    reportes_por_fecha = df.resample('D', on='fecha_del_reporte').size()
    st.line_chart(reportes_por_fecha)

def menu():
    st.title('Análisis de Reportes')
    
    tipo_reporte = st.selectbox(
        'Seleccione el tipo de reporte:',
        ['Agua', 'Salud', 'Electricidad']
    )
    
    df = get_records(tipo_reporte)
    
    if not df.empty:
        grafico_reportes_por_ciudad(df)
        grafico_reportes_por_tipo_averia(df)
        grafico_evolucion_temporal(df)
    else:
        st.warning("No hay reportes registrados para este tipo.")