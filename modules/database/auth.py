import streamlit as st
import sqlite3
import random
import string
import bcrypt
class Auth:
    def __init__(self):
        self.conn = sqlite3.connect('modules/database/users.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                id_number TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def register_admin(self, username, password, first_name, last_name, email, id_number):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.c.execute('INSERT INTO users (username, password, first_name, last_name, email, id_number) VALUES (?, ?, ?, ?, ?, ?)',
                       (username, hashed_password, first_name, last_name, email, id_number))
        self.conn.commit()

    def login_admin(self, username, password):
        self.c.execute('SELECT password FROM users WHERE username = ?', (username, ))
        stored_password = self.c.fetchone()
        if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
            return True
        return False

    def generate_temp_password(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

    def admin_ui(self,action):
        st.subheader("Inicia sesión")
        auth_mode = action

        if auth_mode == "Registrar":
            first_name = st.text_input("Nombres")
            last_name = st.text_input("Apellidos")
            new_username = st.text_input("Nombre de usuario")
            new_password = st.text_input("Contraseña", type="password")
            confirm_password = st.text_input("Confirmar contraseña", type="password")
            email = st.text_input("Correo (tucorreo@123.com)")
            id_number = st.text_input("Cédula (V12234450)")
            if st.button("Registrar"):
                if new_password == confirm_password and new_username and new_password and first_name and last_name and email and id_number:
                    try:
                        self.register_admin(new_username, new_password, first_name, last_name, email, id_number)
                        st.success("Administrador registrado con éxito")
                        return 'registered'
                    except sqlite3.IntegrityError:
                        st.error("El nombre de usuario ya existe")
                elif new_password != confirm_password:
                    st.error("Las contraseñas no coinciden")
                else:
                    st.error("Todos los campos son obligatorios")

        elif auth_mode == "Iniciar sesión":
            username = st.text_input("Nombre de usuario")
            password = st.text_input("Contraseña", type="password")
            if st.button("Iniciar sesión"):
                if self.login_admin(username, password):
                    st.success("Inicio de sesión exitoso")
                    st.write("Bienvenido, administrador")
                    st.session_state.user_type = 'admin'  
                    st.rerun() 
                else:
                    st.error("Nombre de usuario o contraseña incorrectos")
        
            # Opción de recuperar contraseña
            if st.button("Olvidé mi contraseña"):
                st.write("Ingrese su correo electrónico registrado para recuperar la contraseña.")
                recover_email = st.text_input("Correo electrónico")
                if st.button("Enviar"):
                    temp_password = self.generate_temp_password()
                    st.success(f"Su nueva contraseña temporal es: {temp_password}")
                    self.c.execute('UPDATE admins SET password = ? WHERE email = ?', (bcrypt.hashpw(temp_password.encode('utf-8'), bcrypt.gensalt()), recover_email))
                    self.conn.commit()
                    return 'pass_changed'




