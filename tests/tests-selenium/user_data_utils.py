import os
import json

filename='resources/user_data.json'

def save_user_data(user,email, passw):
    user_data = {
        'user':user,
        'email': email,
        'password': passw
    }

    # Crear directorio si no existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Guardar los datos en el archivo JSON
    with open(filename, 'w') as file:
        json.dump(user_data, file)

def load_user_data():
    with open(filename, 'r') as file:
        return json.load(file)

def update_user_password(new_password):
    # Leer los datos existentes
    try:
        with open(filename, 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Actualizar la contraseña
    user_data['password'] = new_password

    # Guardar los datos actualizados
    with open(filename, 'w') as file:
        json.dump(user_data, file)
        
def update_user(new_user):
    # Leer los datos existentes
    try:
        with open(filename, 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Actualizar la contraseña
    user_data['user'] = new_user

    # Guardar los datos actualizados
    with open(filename, 'w') as file:
        json.dump(user_data, file)