import streamlit as st
import pandas as pd
from pandas.api.types import(
    is_object_dtype,
    is_numeric_dtype,
    is_datetime64_dtype,
    is_string_dtype,
    is_datetime64_any_dtype
)

def mostrar_con_filtro(df: pd.DataFrame):

    #Crea un contenedor, en el que estara el dataframe filtrado
    container = st.container()

    df = df.copy()

    with container:
        
        columna_filtro = st.multiselect("Seleccione los filtros:", 
                                        [df.columns[0], df.columns[2], df.columns[3],
                                         df.columns[4], df.columns[5],df.columns[6]])
        
        for columna in columna_filtro:

            if is_string_dtype(df[columna]):
                categorias = st.multiselect(f"Seleccione los datos de {columna}:", df[columna].unique(), df[columna].unique())
                df = df[df[columna].isin(categorias)]

            elif is_numeric_dtype(df[columna]):
                maximo = int(df[columna].max())
                minimo = int(df[columna].min())

                deslizador = st.slider(f"Seleccione los valores de {columna}", minimo, maximo, (minimo, maximo), 1)

                df = df[df[columna].between(*deslizador)]

            elif is_datetime64_any_dtype(df[columna]):
                fecha = st.date_input(f'Seleccione las fechas de {columna}',
                                      value= (df[columna].min(), df[columna].max()))
                
                if len(fecha) == 2:
                    fecha = tuple(map(pd.to_datetime,fecha))
                    inicio, fin = fecha
                    df = df[df[columna].between(inicio,fin)]

    return df
