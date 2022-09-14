from xml.dom.minidom import Document


def get_name():
    number = input('Enter the document number')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'No dicument with this number was found'


def get_shelf():
    number = input('Enter the document number')
    for shelf_key in directories:
        if number in directories.get(shelf_key):
            return shelf_key
    return 'There is no document with this number on the shelves'


def get_list():
    for doc in documents:
        return doc


def add_doc():
    shelf = input('Enter the number of the shelf where u want to put the document: ')
    if shelf not in directories:
        return 'There is no such shelf'
    doc = {}
    doc["type"] = input('Add a document type: ')
    doc["number"] = input('Add a document number: ')
    doc["name"] = input('Add Name: ')
    return doc



documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


while True:
    print('Available commands: p, s, l, a, end')
    comand_code = input('Enter command name: ')

    if comand_code == 'p':
        print(get_name())

    elif comand_code == 's':
        print(get_shelf())
    
    elif comand_code == 'l':
        print(get_list())

    elif comand_code == 'a':
        print(add_doc())

    elif comand_code == 'end':
        break