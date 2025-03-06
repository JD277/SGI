import streamlit as st
import pandas as pd
import Clasificacion.clasificacion as cl
import random
import Clasificacion.Conversion as con
import json
import datetime
from PIL import Image
from firebase_admin import firestore

db = firestore.client()

img = [Image.open('img5.png'), Image.open('img6.png'), Image.open('img8.png')]


def mostrar_reportes_como_tabla(tipo_reporte):
    reportes_ref = db.collection(tipo_reporte)
    reportes = reportes_ref.stream()
    
    reportes_lista = [reporte.to_dict() for reporte in reportes]
    
    if not reportes_lista:
        st.warning(f"No hay reportes registrados para {tipo_reporte}.")
        return
    
    df = pd.DataFrame(reportes_lista)
    
    df['fecha_de_la_averia'] = pd.to_datetime(df['fecha_de_la_averia'])
    df['fecha_del_reporte'] = pd.to_datetime(df['fecha_del_reporte'])

    check = st.checkbox("¿Filtrar datos?", help= '''Si desea ordenar algún dato en particular
                            de mayor a menor o viceversa, presione en el label''')
    
    if check:
        df = cl.mostrar_con_filtro(df)
    
    st.write(f"Reportes de {tipo_reporte}:")
    st.dataframe(df)


def main():
    st.title('Panel de Reportes')

    index = 0
    seleccion = st.selectbox('Elija el servicio a inspeccionar',('Agua','Electricidad','Salud'),index= None, placeholder= 'Seleccione un servicio')
    columnas= st.columns(len(img))

    for columna in columnas:
        with columna:
            st.image(img[index], width= 750)
            index += 1

    if seleccion != None:
 
        #Se muestra una tabla del servicio seleccionado 
        #TODO: Agregar opcion para mostrar una tabla con todos los servicios a la vez
        match seleccion:

            case 'Agua':
                mostrar_reportes_como_tabla('Agua')

            case 'Electricidad':
                mostrar_reportes_como_tabla('Electricidad')

            case 'Salud':
                mostrar_reportes_como_tabla('Salud')

    
    

