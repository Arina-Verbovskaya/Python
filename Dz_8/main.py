import json
import os


def choose_data_type():
    type_data = None
    flag = True
    while flag:
        print('Выбирете какие данные добавить: ', '1 - mobilephone',
              '2 - workphone', '3 - email', '4 - birthday', sep='\n')
        type_data = input('Выбирете цифру (тип телефона): ')
        match type_data:
            case '1':
                type_data = 'mobilephone'
                flag = False
            case '2':
                type_data = 'workphone'
                flag = False
            case '3':
                type_data = 'email'
                flag = False
            case '4':
                type_data = 'birthday'
                flag = False
            case _: flag = True
    return type_data


def menu():  # 0 - выход из программы
    print('Меню: ',
          '0 - выход из программы',
          '1 - сохранить в удаленном хранилище',
          '2 - загрузить данные из удаленного хранилища',
          '3 - вывести по ФИО все данные контакта',
          '4 - вывести по ФИО телефоны',
          '5 - вывести все контакты',
          '6 - создать новый контакт',
          '7 - удалить контакт',
          '8 - редактировать контакт',
          '9 - добавить контактые данные', sep='\n')


def save(phone_book):  # 1 - сохранить в удаленном хранилище
    os.system('cls||clear')
    with open('phone_book.json', 'w', encoding='utf-8') as pb:
        pb.write(json.dumps(phone_book, ensure_ascii=False, indent=4))
    print('\nТелефонная книга успешно сохранена в удаленное хранилище\n')


def load():  # 2 - загрузить данные из удаленного хранилища
    os.system('cls||clear')
    with open('phone_book.json', 'r', encoding='utf-8') as pb:
        pb_local = json.load(pb)
    print('\nТелефонная книга из удаленного хранилища успешно загружена\n')
    return pb_local


def print_all_data_contact():  # 3 - вывести по ФИО все данные контакта
    pb_local = load()
    print_all_fullname()
    f_name = pb_local.get(
        input("Введите ФИО для поиска всех данных: ").lower().strip(), None)
    if f_name != None:
        for k, v in f_name.items():
            if type(v) == list:
                for i in range(len(v)):
                    print(k, v[i], sep=' ', end='\n')
            else:
                print(k, v)
    else:
        print('\nТакого контакта нет')
    print()


def print_phones_contact():  # 4 - вывести по ФИО телефоны
    pb_local = load()
    print_all_fullname()
    f_name = pb_local.get(
        input("Введите ФИО для поиска всех телефонов: ").lower().strip(), None)
    if f_name != None:
        for k, v in f_name.items():
            if (k == 'mobilephone' or k == 'workphone') and type(v) == list:
                for i in range(len(v)):
                    print(k, v[i], sep=' ', end='\n')
            elif k == 'mobilephone' or k == 'workphone':
                print(k, v, sep=' ', end='\n')
    else:
        print('\nТакого контакта нет')
    print()


def print_all_fullname():  # 5 - вывести все контакты
    os.system('cls||clear')
    pb_local = load()
    print("Список контактов в телефонной книге:")
    [print(' ', k) for k in pb_local.keys()]
    print()


def create_new_contant():  # 6 - создать новый контакт
    pb_local = load()
    print_all_fullname()
    print('Введите ФИО нового контакта по образцу: Иванов Иван Иванович')
    f_name = input("Введите ФИО: ").lower().strip()
    if f_name in pb_local:
        return print("\033[31m {} \033[0m" .format('\nТакой контакт существует. Выбирете пункт 9 в меню - добавить контактые данные\n'))

    type_data = choose_data_type()

    inp_data = input("Введите данные: ")
    pb_local.update(
        {f_name: {'mobilephone': [], 'workphone': [], 'email': [], 'birthday': []}})
    pb_local[f_name][type_data].append(inp_data)

    save(pb_local)
    print('Создан контакт и добавлены данные\n')


def delete_contact():  # 7 - удалить контакт
    pb_local = load()
    print_all_fullname()

    print('\nОбразец для ввода ФИО: Иванов Иван Иванович')
    f_name = input(
        "Введите ФИО, контака который вы хотите удалить: ").lower().strip()
    answer = pb_local.get(f_name, None)
    if answer != None:
        pb_local.pop(f_name)
        save(pb_local)
        print('Контакт удалён.\n')
    else:
        print('\nТакого контакта нет\n')


def edit_contact():  # 8 - редактировать телефонную книгу
    pb_local = load()
    print_all_fullname()

    f_name = input(
        "Введите ФИО контакта который вы хотите редактировать: ").lower().strip()
    answer = pb_local.get(f_name, None)
    if answer != None:
        count = 0
        dict_res = {}
        print('\nСписок данных доступных для изменения: ')
        for k, v in pb_local[f_name].items():
            if type(v) == list:
                if v == []:
                    dict_res[count] = [k, v]
                    print(count, k, v)
                    count += 1
                else:
                    for i in v:
                        dict_res[count] = [k, i]
                        print(count, k, i)
                        count += 1
            else:
                dict_res[count] = [k, v]
                print(count, k, v)
                count += 1

        type_data = None
        flag = True
        while flag:
            type_data = int(
                input('Выбирете цифру (0, 1, 2 ...). Данные, которые хотите изменить: '))
            if dict_res.get(type_data, 0) != 0:
                try:
                    position = pb_local[f_name][dict_res[type_data][0]].index(
                        dict_res[type_data][1])
                except:
                    position = -1

                if position >= 0:
                    pb_local[f_name][dict_res[type_data][0]
                                     ][position] = input('Введите новые данные: ')
                else:
                    pb_local[f_name][dict_res[type_data][0]] = [
                        (input('Введите новые данные: '))]

                flag = False

        save(pb_local)
        print('Контакт отредактирован\n')
    else:
        print('\nТакого контакта нет\n')


def add_data():  # 9 - добавить контактые данные
    pb_local = load()
    print_all_fullname()

    f_name = input(
        "В какой контакт вы хотите добавить данные: ").lower().strip()
    type_data = choose_data_type()
    inp_data = input("Введите данные для добавления: ")
    if type(pb_local[f_name][type_data]) == list:
        pb_local[f_name][type_data].append(inp_data)
    else:
        pb_local[f_name][type_data] = inp_data

    save(pb_local)
    print('\nНовые данные добавлены\nТелефонная книга успешно сохранена в удаленное хранилище\n')


try:
    phone_book = load()
except:
    phone_book = {
        "иванов иван иванович": {"mobilephone": ["79370757270", "79370756666"], "birthday": ["13-08-1984"], "email": ["ivan_v@yandex.ru"]},
        "петров петр петрович": {"mobilephone": ["79161100000", "79161122222"], "birthday": ["01-01-1990"], "email": ["petr_p@yandex.ru"]}}
    save(phone_book)
    print("Не удалось загрузить телефонную книгу. Создана тестовая телефонная книга.\n")

choice = None
while choice != 0:
    menu()
    choice = int(input("Введите пункт меню (цифру): "))
    match choice:
        case 0: print('\nВы вышли из программы. До свидания')
        case 1: save(phone_book)
        case 2: load()
        case 3: print_all_data_contact()
        case 4: print_phones_contact()
        case 5: print_all_fullname()
        case 6: create_new_contant()
        case 7: delete_contact()
        case 8: edit_contact()
        case 9: add_data()
        case _: print("\nВыбирете пункт меню или выйдите из программы (Цифра: 0)\n")
