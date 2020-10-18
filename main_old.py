import json

def exit_program():
    exit()

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def enter_number():
    num = input('Captura la opción: ')
    while not is_number(num):
        num = input('Ingresa una opción válida: ')
    return int(num)

def enter_string(message):
    answer = input(message)
    while (not answer):
        answer = input(message)
    return answer

def show_all_users():
    users = read_file()
    print('id\tusername\tpassword\tfullName\trol')
    for user in users:
        row = f'{str(users.index(user) + 1)} '
        for _, value in user.items():
            row += f'{value} '
        print(f'{row}')
    users_menu()

def show_user_data(user):
    for key, value in user.items():
        print(f'{key}: {value}')
    print()

def read_file():
    with open('users.json') as users_file:
        users = json.load(users_file)
        return users

def write_file(user_data):
    with open('users.json', 'w') as users_file:
        # users =
        json.dump(user_data, users_file)

def search_user(username = '', password = ''):
    users = read_file()
    return True

def users_menu():
    print("""
        \nElige la opción:
        1. Editar usuario
        2. Regresar
        3. Salir
    """)
    option = enter_number('Elige la opción: ')
    switcher = {
        1: update_user,
        2: menu,
        3: exit_program,
    }
    return switcher.get(option, users_menu)()

def menu_role():
    print("""
        Elija el rol:
        1. Administrador
        2. Operativo
        3. Usuario
    """ )
    role_option = enter_number()

    switcher_role = {
        1: "Administrador",
        2: "Operativo",
        3: "Usuario",
    }
    return switcher_role.get(role_option, menu_role)

def create_user():
    username = enter_string('Ingrese el username: ')
    password = enter_string('Ingrese la contraseña: ')
    full_name = enter_string('Ingrese el nombre completo: ')
    role = menu_role()

    user_data = {
        'username': username,
        'password': password,
        'fullName': full_name,
        'role': role
    }
    users = read_file()
    users.append(user_data)
    write_file(users)
    print('¡Usuario creado con éxito!\n')
    menu()

def update_user(user_id):
    # enter_number()
    print('¡Usuario actualizado con éxito!\n')
    menu()

def delete_user(user_id):
    users = read_file()
    users.pop(user_id - 1)
    print('¡Usuario eliminado con éxito!\n')
    menu()

def menu():
    print("""
        Elige la opción a realizar:
        1. Crear usuario
        2. Consultar lista de usuarios
        3. Salir
    """)
    option = enter_number()
    switcher = {
        1: create_user,
        2: show_all_users,
        3: exit_program,
    }
    return switcher.get(option, menu)()

def login():
    print('¡Bienvenido!\n')
    username = enter_string('Ingresa tu usuario:  ')
    password = enter_string('Ingresa una contraseña:  ')

    if search_user(username, password):
        menu()
    else:
        print('Usuario y/o contraseñas incorrectos')
        login()

if (__name__ == "__main__"):
    menu()
