import csv
import os
import re


def read_file():
    os.makedirs('notebook', exist_ok=True)
    with open(os.path.join('notebook', 'notebook.csv'), 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        readers = list(reader)
        while True:
            try:
                readers.remove([])
            except ValueError:
                break
        return readers


def main_menu():
    print(f'На данный момент в записной книжке {len(read_file()) - 1} контактов')
    while True:
        print(
            '   1. Добавить запись\n'
            '   2. Удалить запись\n'
            '   3. Изменить запись\n'
            '   4. Поиск\n'
            '   5. Сортировка\n'
            '   6. Выход\n'
        )
        inputs = input('Cделайте Ваш выбор: ')
        if inputs == '1':
            add_note()
        elif inputs == '2':
            delete_note()
        elif inputs == '3':
            change_note()
        elif inputs == '4':
            search()
        elif inputs == '5':
            sorter()
        elif inputs == '6':
            print('Завершение работы')
            break
        else:
            print('Неверный ввод данных')


def sorter():
    os.makedirs('notebook', exist_ok=True)
    with open(os.path.join('notebook', 'notebook.csv'), 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        readers = list(reader)
    sort_contact = input("Введите параметр по котоому хотите отсортировать контакты ИМЯ или ФАМИЛИЯ > ").title()
    sorted_contact = sorted(readers, key=lambda i: i[sort_contact])
    with open(os.path.join('notebook', 'notebook.csv'), 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for valuer in sorted_contact:
            writer.writerow(valuer.values())


def search():
    search_contact = input("Введите ИМЯ или номер телефона контакта который хотите найти > ").title()
    if len(search_contact) == 1:
        for surname in read_file()[1::]:
            found = re.match(r'[А-Я]\w+', surname[1])
            if found[0][0] == search_contact:
                print(surname)
    else:
        for row in read_file():
            if row[0] == search_contact or row[2] == search_contact:
                print(row)


def checker(user_input, count):
    while True:
        if count == 0 or count == 1 or count == 2:
            if user_input == '':
                print('Это обязательное поле для ввода')
                user_input = input('> ').title()
            else:
                return user_input
        else:
            return user_input


def change_note():
    read_list = []
    read_list2 = []
    idx = 0
    change_contact = input("Введите ИМЯ и ФАМИЛИЮ (или номер телефона) контакта который хотите изменить > ").title()
    for row in read_file():
        if f'{row[0]}{row[1]}' == change_contact or row[2] == change_contact:
            for head in header:
                print(f'{head}: {row[idx]}')
                read_list.append(checker(input('> ').title(), idx))
                idx += 1
        else:
            read_list2.append(row)
        with open(os.path.join('notebook', 'notebook.csv'), 'w', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(read_list2)
            writer.writerow(read_list)


def delete_note():
    line = []
    delete_contact = input("Введите ИМЯ и ФАМИЛИЮ (или номер телефона) контакта который хотите удалить > ")
    for row in read_file():
        if f'{row[0]} {row[1]}' == delete_contact or row[2] == delete_contact:
            print('Запись удалена')
        else:
            line.append(row)
    with open(os.path.join('notebook', 'notebook.csv'), 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(line)


def add_note():
    count = 0
    _list = []
    with open(os.path.join('notebook', 'notebook.csv'), 'a', encoding='utf8') as f:
        writer = csv.writer(f)
        for row in header:
            print(row)
            _list.append(checker(input('> ').title(), count))
            count += 1
        writer.writerow(_list)


if __name__ in '__main__':
    header = ['Имя', 'Фамилия', 'Номер телефона', 'Адрес', 'Дата рождения']
    main_menu()
