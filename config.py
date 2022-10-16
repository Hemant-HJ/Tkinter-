import json

def file_load():
    with open('variable.json', 'r') as file:
        data = json.load(file)
    return data

data = file_load()

USERNAME = data['username']
PASSWORD = data['password']
HOST = data['host']
DATABASE = data['database']
PORT = data['port']
STARTED = data['started']

def file_write(changed_data):
    with open('variable.json', 'w') as file:
        data.update(changed_data)
        json.dump(data, file, indent = 4)
        return True
    return False