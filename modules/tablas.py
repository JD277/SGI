import streamlit as st
import pandas as pd
import modules.Clasification.clasification as cl
import modules.Clasification.Converision as con
from PIL import Image

img = [Image.open('images/img5.png'), Image.open('images/img6.png'), Image.open('images/img8.png')]

class Tables():
    def __init__(self, db):
        self.db = db
    def mostrar_reportes_como_tabla(self,tipo_reporte):
        reportes_lista = self.db.get_report_by_service(tipo_reporte)
        
        if not reportes_lista:
            st.warning(f"No hay reportes registrados para {tipo_reporte}.")
            return
        
        df = pd.DataFrame(reportes_lista)
        
        df['date_of_failure'] = pd.to_datetime(df['date_of_failure'])
        df['date_of_record'] = pd.to_datetime(df['date_of_record'])

        check = st.checkbox("¿Filtrar datos?", help= '''Si desea ordenar algún dato en particular
                                de mayor a menor o viceversa, presione en el label''')
        
        if check:
            df = cl.mostrar_con_filtro(df)
        
        st.write(f"Reportes de {tipo_reporte}:")
        st.dataframe(df)


    def main(self):
        st.title('Panel de Reportes')

        index = 0
        seleccion = st.selectbox('Elija el servicio a inspeccionar',('Agua', 'Electricidad', 'Vialidad','Educacion','Comunicacion','Transporte','Seguridad','Saneamiento'),index= None, placeholder= 'Seleccione un servicio')


        if seleccion != None:
    
            #Se muestra una tabla del servicio seleccionado 
            #TODO: Agregar opcion para mostrar una tabla con todos los servicios a la vez
            match seleccion:

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

