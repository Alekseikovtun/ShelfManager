from package_data.data import inp_directories, inp_documents


def add_doc():
    shelf = input('Enter the number of the \
    shelf where u want to put the document: ')
    if shelf not in inp_directories:
        return 'There is no such shelf'
    doc = {}
    doc["type"] = input('Add a document type: ')
    doc["number"] = input('Add a document number: ')
    doc["name"] = input('Add Name: ')
    inp_documents.append(doc)
    inp_directories[shelf].append(doc['number'])
    return inp_documents, inp_directories
