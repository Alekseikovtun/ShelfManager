import typing


inp_documents = [
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

inp_directories = {'3': []}  # type: typing.Dict[str, typing.List[str]]


def test_add_doc1():
    shelf = '3'
    print(f'Shelf {shelf}')
    if shelf not in inp_directories:
        return 'There is no such shelf'
    doc = {}
    doc["type"] = 'PASS'
    doc["number"] = '123123'
    doc["name"] = 'FTN'
    inp_documents.append(doc)
    inp_directories[shelf].append(doc['number'])
    assert inp_documents == [
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "PASS", "number": "123123", "name": "FTN"}
    ], inp_directories == {
        '3': ['123123']
    }
