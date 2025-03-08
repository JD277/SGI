import streamlit as st
# import sqlite3
# import random
# import string
# import bcrypt

# # Crea la base de datos 
# conn = sqlite3.connect('users.db')
# c = conn.cursor()
# c.execute('''
#     CREATE TABLE IF NOT EXISTS admins (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         email TEXT NOT NULL,
#         id_number TEXT NOT NULL
#     )
# ''')
# conn.commit()

# # Funciones para registrar y verificar credenciales
# def register_admin(username, password, first_name, last_name, email, id_number):
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     c.execute('INSERT INTO admins (username, password, first_name, last_name, email, id_number) VALUES (?, ?, ?, ?, ?, ?)',
#               (username, hashed_password, first_name, last_name, email, id_number))
#     conn.commit()

# def login_admin(username, password):
#     c.execute('SELECT password FROM admins WHERE username = ?', (username,))
#     stored_password = c.fetchone()
#     if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
#         return True
#     return False

# def generate_temp_password(length=8):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for i in range(length))

# # Interfaz 
# st.title("Sistema de Reportes de Servicios Públicos")
# user_type = st.radio("Ingresar como:", ("Usuario", "Administrador"))

# def admin_ui():
#     st.subheader("Inicio de sesión para administradores")
#     auth_mode = st.selectbox("¿Qué desea hacer?", ["Iniciar sesión", "Registrar nuevo administrador"])

#     if auth_mode == "Registrar nuevo administrador":
#         first_name = st.text_input("Nombres")
#         last_name = st.text_input("Apellidos")
#         new_username = st.text_input("Nombre de usuario")
#         new_password = st.text_input("Contraseña", type="password")
#         confirm_password = st.text_input("Confirmar contraseña", type="password")
#         email = st.text_input("Correo")
#         id_number = st.text_input("Cédula")
#         if st.button("Registrar"):
#             if new_password == confirm_password and new_username and new_password and first_name and last_name and email and id_number:
#                 try:
#                     register_admin(new_username, new_password, first_name, last_name, email, id_number)
#                     st.success("Administrador registrado con éxito")
#                 except sqlite3.IntegrityError:
#                     st.error("El nombre de usuario ya existe")
#             elif new_password != confirm_password:
#                 st.error("Las contraseñas no coinciden")
#             else:
#                 st.error("Todos los campos son obligatorios")

#     elif auth_mode == "Iniciar sesión":
#         username = st.text_input("Nombre de usuario")
#         password = st.text_input("Contraseña", type="password")
#         if st.button("Iniciar sesión"):
#             if login_admin(username, password):
#                 st.success("Inicio de sesión exitoso")
#                 st.write("Bienvenido, administrador")
#                 # Aqui se puede añadir a donde se quiere redirigir la pagina cuando se ingrese como admin
#             else:
#                 st.error("Nombre de usuario o contraseña incorrectos")
        
#         # Opción de recuperar contraseña
#         if st.button("Olvidé mi contraseña"):
#             st.write("Ingrese su correo electrónico registrado para recuperar la contraseña.")
#             recover_email = st.text_input("Correo electrónico")
#             if st.button("Enviar"):
#                 temp_password = generate_temp_password()
#                 st.success(f"Su nueva contraseña temporal es: {temp_password}")
#                 c.execute('UPDATE admins SET password = ? WHERE email = ?', (bcrypt.hashpw(temp_password.encode('utf-8'), bcrypt.gensalt()), recover_email))
#                 conn.commit()

# def user_ui():
#     st.subheader("Bienvenido, Usuario")
#     st.write("Esta sección está reservada para funcionalidades de usuarios.")
#     # Aqui se puede añadir a donde se quiere redirigir la pagina cuando se ingrese como usuario
# if user_type == "Administrador":
#     admin_ui()
# else:
#     user_ui()

# conn.close()
from modules.database.dbmanager import DbManager
@st.cache_resource  # ¡Muy importante!
def get_db_manager():
    return DbManager(
        'modules/database/estructuras.json',
        'https://estructuras-9be66-default-rtdb.firebaseio.com/'
    )

db_manager = get_db_manager()

import modules.inicio as inicio
import modules.objetivo as objetivo
from modules.report import Report_screen
# import modules.monitoreo as monitoreo
# import modules.tablas as tablas
# import modules.metricas as metricas

st.set_page_config(page_title='Gestion de Servicios Publicos', layout='centered', initial_sidebar_state='collapsed')

def main():
    menu = ['Inicio', 'Objetivo', 'Reportes', 'Monitoreo', 'Panel de Reportes', 'Metricas y Resultados']
    icons = {
        "Inicio": ":material/house:",
        "Objetivo": ":material/emoji_objects:",
        "Reportes": ":material/report:",
        "Monitoreo": ":material/monitoring:",
        "Panel de Reportes": ":material/browse_activity:",
        "Metricas y Resultados": ":material/trending_up:"
    }

    st.sidebar.title(':blue-background[Menu de seleccion]')
    choice = st.sidebar.radio('Seleccione una opcion', [f"{icons[item]} {item}" for item in menu])

    if choice.startswith(":material/house:"):
        inicio.inicio()

    elif choice.startswith(":material/emoji_objects:"):
        objetivo.obj()

    elif choice.startswith(":material/report:"):
        report = Report_screen(db_manager)
        report.menu()

    # elif choice.startswith(":material/monitoring:"):
    #     monitoreo.menu()

    # elif choice.startswith(":material/browse_activity:"):
    #     tablas.main()
    
    # elif choice.startswith(":material/trending_up:"):
    #     metricas.menu() 
        
if __name__ == '__main__':
    main()
