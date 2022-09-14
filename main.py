from xml.dom.minidom import Document


def get_name():
    number = input('Введите номер документа')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документа с таким номером не найдено'


def get_shelf():
    number = input('Введите номер документа')
    for shelf_key in directories:
        if number in directories.get(shelf_key):
            return shelf_key
    return 'На полках с нет документа с таким номером'


def get_list():
    for docs in documents:
        return docs


def add_doc():
    shelf = input('Введите номер полки, куда хотите положить документ: ')
    if shelf not in directories:
        return 'Нет такой полки'
    doc = {}
    for docs_info in ('type, )
    return



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

