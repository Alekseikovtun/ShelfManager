from package_data.data import inp_documents


def get_name():
    number = input('Enter the document number: ')
    for data in inp_documents:
        if data.get("number") == number:
            return data.get('name')
    return 'No dicument with this number was found'