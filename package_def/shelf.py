from package_data.data import inp_directories, inp_documents


def get_shelf():
    number = input('Enter the document number: ')
    for shelf_key in inp_directories:
        if number in inp_directories.get(shelf_key):
            return shelf_key
    return 'There is no document with this number on the shelves'