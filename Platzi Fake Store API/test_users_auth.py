import requests

# URL base de la API
BASE_URL = "https://api.escuelajs.co/api/v1"

# Credenciales de autenticación
credentials = {
    "email": "john@mail.com",
    "password": "changeme"
}

# Función para obtener tokens
def get_tokens():
    auth_url = f"{BASE_URL}/auth/login"
    response = requests.post(auth_url, json=credentials)

    if response.status_code in [200, 201]:
        data = response.json()
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")
        if access_token:
            print(f"Access Token: {access_token[:10]}...")
            print(f"Refresh Token: {refresh_token[:10]}...")
            return access_token, refresh_token
        else:
            print("No se obtuvo el token de acceso.")
    else:
        print(f"Error en la autenticación. Código de estado: {response.status_code}")
    return None, None

# Función para obtener todos los usuarios
def get_all_users(access_token):
    users_url = f"{BASE_URL}/users"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(users_url, headers=headers)

    if response.status_code == 200:
        users = response.json()
        print(f"Usuarios obtenidos: {len(users)}")
    else:
        print(f"Error al obtener usuarios. Código de estado: {response.status_code}, Respuesta: {response.text}")

# Función para obtener un usuario específico por ID
def get_user_by_id(access_token, user_id):
    user_url = f"{BASE_URL}/users/{user_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(user_url, headers=headers)

    if response.status_code == 200:
        user = response.json()
        print(f"Usuario obtenido: ID: {user['id']}, Nombre: {user['name']}")
    else:
        print(f"Error al obtener el usuario. Código de estado: {response.status_code}, Respuesta: {response.text}")

# Función para crear un nuevo usuario
def create_user(access_token, user_data):
    create_url = f"{BASE_URL}/users"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(create_url, json=user_data, headers=headers)

    if response.status_code == 201:
        new_user = response.json()
        print(f"Usuario creado: ID: {new_user['id']}, Nombre: {new_user['name']}")
        return new_user['id']
    else:
        print(f"Error al crear el usuario. Código de estado: {response.status_code}, Respuesta: {response.text}")
    return None

# Función para actualizar un usuario existente
def update_user(access_token, user_id, updated_data):
    update_url = f"{BASE_URL}/users/{user_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.put(update_url, json=updated_data, headers=headers)

    if response.status_code == 200:
        updated_user = response.json()
        print(f"Usuario actualizado: ID: {updated_user['id']}, Nombre: {updated_user['name']}")
    else:
        print(f"Error al actualizar el usuario. Código de estado: {response.status_code}, Respuesta: {response.text}")

# Función para verificar la disponibilidad de un correo electrónico
def check_email_availability(access_token, email):
    check_url = f"{BASE_URL}/users/is-available"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(check_url, json={"email": email}, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        result = response.json()
        is_available = result.get("isAvailable")
        print(f"El correo electrónico '{email}' está {'disponible' if is_available else 'no disponible'}.")
    else:
        print(f"Error al verificar el correo electrónico. Código de estado: {response.status_code}, Respuesta: {response.text}")

# Ejemplo de uso
def main():
    access_token, _ = get_tokens()

    if access_token:
        get_all_users(access_token)
        get_user_by_id(access_token, 1)

        new_user_data = {
            "name": "Nicolas",
            "email": "nico@gmail.com",
            "password": "1234",
            "avatar": "https://picsum.photos/800"
        }
        new_user_id = create_user(access_token, new_user_data)

        if new_user_id:
            update_user_data = {
                "name": "Change name"
            }
            update_user(access_token, new_user_id, update_user_data)

        check_email_availability(access_token, "john@mail.com")

if __name__ == "__main__":
    main()
