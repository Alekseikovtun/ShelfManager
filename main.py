class ShelfManager:

    def __init__(self, docs, dirs):
        self.documents = docs
        self.directories = dirs
        print(id(docs), id(self.documents))

    def get_name(self):
        number = input('Enter the document number')
        for data in self.documents:
            if data.get("number") == number:
                return data.get('name')
        return 'No dicument with this number was found'

    def get_shelf(self):
        number = input('Enter the document number')
        for shelf_key in self.directories:
            if number in self.directories.get(shelf_key):
                return shelf_key
        return 'There is no document with this number on the shelves'

    def get_list(self):
        return (id(self.documents))

    def add_doc(self):
        shelf = input('Enter the number of the shelf where u want to put the document: ')
        if shelf not in self.directories:
            return 'There is no such shelf'
        doc = {}
        doc["type"] = input('Add a document type: ')
        doc["number"] = input('Add a document number: ')
        doc["name"] = input('Add Name: ')
        self.documents.append(doc)
        self.directories[shelf].append(doc['number'])
        return self.documents, self.directories

    def start(self):
        while True:
            print('Available commands: people, shelf, list, add, end')
            comand_code = input('Enter command name: ')
                
            if comand_code == 'people':
                print(self.get_name())
            elif comand_code == 'shelf':
                print(self.get_shelf())
            elif comand_code == 'list':
                print(self.get_list())
            elif comand_code == 'add':
                print(self.add_doc())
            elif comand_code == 'end':
                break
            else:
                print('Command not found:', comand_code) 



inp_documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

inp_directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

print(id(inp_documents))
addshelves_0 = ShelfManager(inp_documents, inp_directories)
addshelves_0.start()
addshelves_1 = ShelfManager(inp_documents, inp_directories)
addshelves_1.start()
print(addshelves_0.get_list())
print(addshelves_1.get_list())

