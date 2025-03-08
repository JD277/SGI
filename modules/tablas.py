import streamlit as st
import pandas as pd
import modules.Clasification.clasification as cl
from modules.AI.AIComponent import *
from PIL import Image
from modules.database.dbmanager import DbManager
img = [Image.open('images/img5.png'), Image.open('images/img6.png'), Image.open('images/img8.png')]

class Tables():
    def __init__(self, db:DbManager):
        self.db = db
        self.data = None
    def mostrar_reportes_como_tabla(self,tipo_reporte):
        reportes_final = []
        if tipo_reporte != 'Todos':
            reportes_lista = self.db.get_report_by_service(tipo_reporte)
            reportes_final = reportes_lista
        else:
            reportes_lista = self.db.read_record() 
            if reportes_lista is None:
                st.warning("No hay reportes registrados.")
                return
            for reporte in reportes_lista:
                    reportes_final.append(reportes_lista[reporte])
            
        
        if not reportes_final:
            st.warning(f"No hay reportes registrados para {tipo_reporte}.")
            return
        
        self.df = pd.DataFrame(reportes_final)
        
        self.df['date_of_failure'] = pd.to_datetime(self.df['date_of_failure'])
        self.df['date_of_record'] = pd.to_datetime(self.df['date_of_record'])

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
    
            #Se muestra una tabla del servicio seleccionado 
            match seleccion:

                case 'Todos':
                    self.mostrar_reportes_como_tabla('Todos')

                case 'Agua':
                    self.mostrar_reportes_como_tabla('Agua')

                case 'Electricidad':
                    self.mostrar_reportes_como_tabla('Electricidad')

                case 'Salud':
                    self.mostrar_reportes_como_tabla('Salud')

                case 'Vialidad':
                    self.mostrar_reportes_como_tabla('Vialidad')
                
                case 'Educacion':
                    self.mostrar_reportes_como_tabla('Educacion')
                
                case 'Comunicacion':
                    self.mostrar_reportes_como_tabla('Comunicacion')
                
                case 'Transporte':
                    self.mostrar_reportes_como_tabla('Transporte')

                case 'Seguridad':
                    self.mostrar_reportes_como_tabla('Seguridad') 

                case 'Saneamiento':
                    self.mostrar_reportes_como_tabla('Saneamiento')


