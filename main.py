from package_def import add, all, people, shelf

if __name__ == '__main__':
    def start():
        while True:
            print('Available commands: people, shelf, all, add, end')
            comand_code = input('Enter command name: ')
            if comand_code == 'p':
                print('\n', people.get_name(), '\n')
            elif comand_code == 's':
                print('\n', shelf.get_shelf(), '\n')
            elif comand_code == 'l':
                print('\n', all.get_list(), '\n')
            elif comand_code == 'a':
                print('\n', add.add_doc(), '\n')
            elif comand_code == 'e':
                break
            else:
                print('Command not found:', comand_code)


start()
