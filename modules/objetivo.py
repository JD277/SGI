import streamlit as st
from PIL import Image

banner2 = Image.open('images/banner2.jpg')
width, heigth = banner2.size
new_height = 600
new_width = 1920
new_banner2 = banner2.resize((new_width, new_height))

img3 = Image.open('images/img3.png')
img4 = Image.open('images/img4.png')

def obj():
    st.title('Monitoreo y Reportes de Incidencias en Servicios Públicos')
    st.write(
        '''
        Nos dedicamos a optimizar el monitoreo y los reportes de incidencias 
        en los servicios públicos esenciales como agua, salud y electricidad. 
        Con nuestra plataforma, buscamos mejorar la calidad, disponibilidad y 
        respuesta a los problemas que afectan a la comunidad, asegurando que 
        las incidencias sean reportadas y solucionadas de manera rápida y 
        eficiente.
        '''
    )
    
    st.image(new_banner2)
    
    st.title('Nuestro Objetivo')
    
    st.write(
            '''
            Nuestro objetivo es optimizar la recolección de datos sobre servicios públicos esenciales como agua, salud y electricidad. Con nuestra plataforma, pretendemos mejorar el monitoreo y seguimiento de estos servicios, facilitando la resolución rápida de problemas y averías.
            '''
        )
    
    st.title('¿Qué Ofrecemos?')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Monitoreo en tiempo real')
        st.write(
            '''
            • Agua: Seguimiento del suministro y calidad del agua.

            • Salud: Información sobre la disponibilidad y estado de los servicios de salud.

            • Electricidad: Estado del suministro eléctrico, incluyendo apagones y mantenimiento.
            '''
        )
        st.subheader('Facilitar el Seguimiento de Averías')
        st.write(
            '''
            • Reportes por personal autorizado: Los reportes de problemas serán realizados por el personal de la compañía a través de llamadas con los afectados, asegurando precisión y seguimiento adecuado.
            '''
        )
    
    with col2:
        st.image(img3, width=800)
        
    col1,col2 = st.columns(2)
    with col2:
        st.subheader('Como funciona')
        st.write(
            '''
            • Acceso rápido: El personal autorizado puede acceder a la plataforma desde cualquier dispositivo sin necesidad de registrarse.
            
            • Recoleccion de datos: Captura y almacena datos relacionados con los servicios públicos de manera anónima.
            
            • Acción y Respuesta: Facilita la comunicación entre usuarios y proveedores para una acción rápida y efectiva.
            '''
        )
    with col1:
        st.image(img4, width=800)
    
    st.title('Beneficios')
    st.write(
        '''
        • Eficiencia: Mejora la gestión y resolución de problemas de servicios públicos.

        • Transparencia: Proporciona información clara y accesible sobre el estado de los servicios.

        • Participación Ciudadana: Empodera a los ciudadanos para que contribuyan a la mejora de los servicios públicos de manera anónima.
        '''
    )
    
    st.subheader('¡Explora nuestra plataforma y descubre cómo podemos ayudarte a mejorar la calidad de los servicios públicos en tu comunidad!')