documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки,
# на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
# Задача №2. Дополнительная (не обязательная)
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой

def list_doc_on_directories(directories):
    i = 0
    doc = []
    keys = list(directories.keys())
    for i in range(len(keys)):
        doc += directories[keys[i]]
        i += 1
    return doc


def people(documents, directories):
    doc = input('Введите номер документа - ')
    a = "Документа с таким номером нет на полках."
    i = 0
    host_doc = ''
    if doc in list_doc_on_directories(directories):
        for i in range(len(documents)):
            if doc == documents[i]['number']:
                host_doc = documents[i]['name']
                break
            i += 1
        print('Владелец документа - ', end='')
        return host_doc
    else:
        return a


def list_doc(documents):
    i = 0
    print('Список перечня документов:')
    for i in range(len(documents)):
        print(documents[i]['type'] + ' ' + '"' + documents[i]['number'] + '"' + ' ' + '"' + documents[i]['name'] + '"')
        i += 1


def shelf(documents, directoties):
    doc = input('Введите номер документа - ')
    a = "Документа с таким номером нет на полках."
    i = 0
    h = list(directories.keys())
    if doc in list_doc_on_directories(directories):
        for i in range(len(h)):
            if doc in directories[h[i]]:
                number_shelf = h[i]
                break
            i += 1
        print('Документ находится на полке - ', end='')
        return number_shelf
    else:
        return a


def add_doc(documents, directories):
    type_doc = input()
    number_doc = input()
    name_doc = input()
    shelf_doc = input()
    b = {}
    b.setdefault('type', type_doc)
    b.setdefault('number', number_doc)
    b.setdefault('name', name_doc)
    documents.append(b)

    directories.setdefault(shelf_doc, [])
    directories[shelf_doc] += [number_doc]

    return documents, directories


def del_doc(documents, directories):
    del_doc = input('Учажите документ, который нужно удалить - ')
    i = 0
    b = 'Документа с таким номером нет.'
    if del_doc in list_doc_on_directories(directories):
        for i in range(len(documents)):
            if del_doc == documents[i]['number']:
                documents.pop(i)
                break
            i += 1
        i = 0
        a = list(directories.keys())
        for i in range(len(a)):
            if del_doc in directories[a[i]]:
                directories[a[i]].pop(directories[a[i]].index(del_doc))
                break
            i += 1
        return documents, directories
    else:
        return b


def move_doc(directories):
    move_doc = input('Укажите номер документа, который хотите переместить - ')
    turget_shelf = input('Укажите полку, на которую хотете переместить документ - ')
    i = 0
    a = list(directories.keys())
    b = 'Документа с таким номером нет.'
    if move_doc in list_doc_on_directories(directories):
        for i in range(len(a)):
            if move_doc in directories[a[i]]:
                directories[a[i]].pop(directories[a[i]].index(move_doc))
                break
            i += 1
        directories[turget_shelf] = [move_doc]
        return directories
    else:
        return b


def add_shelf(directories):
    new_shelf = input('Введите название новой полки - ')
    a = 'Такая полка уже существует!'
    if new_shelf in list(directories.keys()):
        print(a)
    else:
        directories[new_shelf] = []
    return directories


if __name__ == '__main__':
    while True:
        command = input('Введите команду - ')
        command_list = ['p', 'l', 's', 'a', 'd', 'm', 'as', 'q']
        info_list = ''' Список доступных команд:
                        p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
                        l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
                        s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
                        a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и 
                        номер полки, на котором он будет храниться. 
                        d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
                        m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
                        as – add shelf – команда, которая спросит номер новой
                        help - помощь - список доступных команд
                        q - quit - выход
                        '''
        if command in command_list:
            if command == 'p':
                print(people(documents, directories))
            if command == 'l':
                list_doc(documents)
            if command == 's':
                print(shelf(documents, directories))
            if command == 'a':
                print(add_doc(documents, directories))
            if command == 'd':
                print(del_doc(documents, directories))
            if command == 'm':
                print(move_doc(directories))
            if command == 'as':
                print(add_shelf(directories))
            if command == 'help':
                print(info_list)
            if command == 'q':
                break
        else:
            print(info_list)
