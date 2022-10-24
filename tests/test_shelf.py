inp_directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def test_get_shelf():
    number = '11-2'
    for shelf_key in inp_directories:
        if number in inp_directories.get(shelf_key):
            assert shelf_key == '1'
