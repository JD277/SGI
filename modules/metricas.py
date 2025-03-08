import streamlit as st
import pandas as pd
class Statics():
    def __init__(self, db:pd.DataFrame):
        self.db = db

    def grafico_reportes_por_ciudad(self,df):
        st.subheader("Reportes por Ciudad")
        reportes_por_ciudad = df['city'].value_counts()
        st.bar_chart(reportes_por_ciudad)

    def grafico_reportes_por_tipo_averia(self,df):
        st.subheader("Reportes por Tipo de Avería")
        reportes_por_tipo = df['service'].value_counts()
        st.bar_chart(reportes_por_tipo)

    def grafico_evolucion_temporal(self,df):
        st.subheader("Evolución de Reportes en el Tiempo")
        df['date_of_record'] = pd.to_datetime(df['date_of_record'])
        reportes_por_fecha = df.resample('D', on='date_of_record').size()
        st.line_chart(reportes_por_fecha)

    def menu(self):
        st.title('Análisis de Reportes')
        
        tipo_reporte = st.selectbox(
            'Seleccione el tipo de reporte:',
            ['Todos','Agua', 'Electricidad', 'Vialidad','Educacion','Comunicacion','Transporte','Seguridad','Saneamiento']
        )
        if tipo_reporte != 'Todos':
            df = self.db[self.db['service'].isin([tipo_reporte])]
        else:
            df = self.db

        
        if not df.empty:
            self.grafico_reportes_por_ciudad(df)
            self.grafico_reportes_por_tipo_averia(df)
            self.grafico_evolucion_temporal(df)
        else:
            st.warning("No hay reportes registrados para este tipo.")