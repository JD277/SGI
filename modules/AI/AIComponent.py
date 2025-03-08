import streamlit as st
from modules.AI.geminiAnalizer import DataAnalyst
def mostrar_input_markdown(df):
    # Campo de entrada
    texto = st.text_input("Preguntale a Gemini 2.0")
    analizer = DataAnalyst()
    
    # Botón para mostrar
    if st.button("Analizar"):
        # Mostramos el contenido como markdown
        answer = analizer.analyze(df,texto)
        st.markdown(answer)
        
