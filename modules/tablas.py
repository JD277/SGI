import streamlit as st
import pandas as pd
import modules.Clasification.clasification as cl
from modules.AI.AIComponent import *

class Tables():
    def __init__(self, db:pd.DataFrame):
        self.db = db
        self.df = db
    def mostrar_reportes_como_tabla(self,tipo_reporte):
        
        if self.db.empty:
            st.warning(f"No hay reportes registrados para {tipo_reporte}.")
            return
        
        check = st.checkbox("¿Filtrar datos?", help= '''Si desea ordenar algún dato en particular
                                de mayor a menor o viceversa, presione en el label''')

        if check:
            self.df = cl.mostrar_con_filtro(self.df)
        
        st.write(f"Reportes de {tipo_reporte}:")
        st.dataframe(self.df)
        
        check2 = st.checkbox("Analizar con Gemini AI", help= '''Analice los datos con la AI de Google Gemini 2.0 para obtener descubrimientos asombrosos''')
        
        if check2:
            self.df = mostrar_input_markdown(self.df)

    def main(self):
        st.title('Panel de Reportes')

        index = 0
        seleccion = st.selectbox('Elija el servicio a inspeccionar',('Todos','Agua', 'Electricidad', 'Vialidad','Educacion','Comunicacion','Transporte','Seguridad','Saneamiento'),index= None, placeholder= 'Seleccione un servicio')


        if seleccion != None:
            self.mostrar_reportes_como_tabla(seleccion)

