# Задача 2. Сервер

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for key, items in server_data.items():
    print('{0}:'.format(key))
    for key_data, data in items.items():
        print('\t{0}: {1}'.format(key_data, data))
