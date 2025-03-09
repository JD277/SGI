import streamlit as st
import modules.objetivo as objetivo
from PIL import Image

banner1 = Image.open('images/banner1.jpeg')
width, heigth = banner1.size
new_height = 600
new_width = 1920
new_banner1 = banner1.resize((new_width, new_height))

img1 = Image.open('images/img1.png')
img2 = Image.open('images/img2.png')

def inicio():
    st.image(new_banner1)
    col1,col2,col3 = st.columns(3)

    with col2:
        boton = st.button("Conoce más sobre nuestro proyecto", key = 'Proyecto')
    if boton:
        objetivo.obj()
    
    if not boton:
        
        
        st.title('Bienvenido a la pagina de Gestión para de Servicios Públicos')
        
        col1,col2 = st.columns(2)
        with col1:
            st.write(
                '''
                
                
                Nuestra plataforma está diseñada para optimizar la recolección de datos sobre 
                los servicios públicos esenciales como agua, salud y electricidad. Con esta 
                herramienta, queremos mejorar el monitoreo y seguimiento de estos servicios, 
                facilitando la resolución rápida de problemas y averías.
                
                Ademas de garantizar una mejor optimizacion al momento de recolectar los datos, también 
                ofrece una serie de beneficios significativos tanto para los usuarios como para 
                la comunidad en general:
                '''
            )
        with col2:
            st.image(img1, width=800)
    
        col1,col2 = st.columns(2)
        with col1:
            st.image(img2, width=800)
        with col2:
            st.write(
                '''
                • Monitoreo en tiempo real: Accede a información actualizada sobre el suministro de agua, el estado de los servicios de salud y la electricidad.

                • Reportes por personal autorizado: Los reportes de problemas serán realizados por el personal de la compañía a través de llamadas con los afectados, asegurando precisión y seguimiento adecuado.

                • Resolución eficiente de problemas: Proporciona canales de comunicación directa para una rápida acción y respuesta por parte de los proveedores de servicios.
                '''
            )
        
        st.subheader('Explora nuestra plataforma y contribuye a mejorar la calidad de los servicios públicos en tu comunidad.')
    