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
    print(f'At this moment in notebook {len(read_file()) - 1} contacts')
    while True:
        print(
            '   1. Add note\n'
            '   2. Delete note\n'
            '   3. Change note\n'
            '   4. Search\n'
            '   5. Sort\n'
            '   6. Exit\n'
        )
        inputs = input('Choose: ')
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
            print('Exit')
            break
        else:
            print('Invalid input')


def sorter():
    os.makedirs('notebook', exist_ok=True)
    with open(os.path.join('notebook', 'notebook.csv'), 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        readers = list(reader)
    sort_contact = input("Input the parameter by which you want to sort contacts FIRST NAME or SURNAME > ").title()
    sorted_contact = sorted(readers, key=lambda i: i[sort_contact])
    with open(os.path.join('notebook', 'notebook.csv'), 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for valuer in sorted_contact:
            writer.writerow(valuer.values())


def search():
    search_contact = input("Input FIRST NAME, PHONE NUMBER or SURNAME FIST LETTER of the contact with you want to find > ").title()
    if len(search_contact) == 1:
        for surname in read_file()[1::]:
            found = re.match(r'[A-Z]\w+', surname[1])
            if found[0][0] == search_contact:
                print(surname)
    elif search_contact.lower() == 'all':
        return list(map(lambda i: print(i), read_file()[1:]))
    else:
        for row in read_file():
            if row[0] == search_contact or row[2] == search_contact:
                print(row)


def checker(user_input, count):
    while True:
        if count == 0 or count == 1 or count == 2:
            if user_input == '':
                print('This is required input field')
                user_input = input('> ').title()
            else:
                return user_input
        else:
            return user_input


def change_note():
    read_list = []
    read_list2 = []
    idx = 0
    change_contact = input("Input FIRST NAME and SURNAME ( or PHONE NUMBER) of the contact with you want to change > ").title()
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
    delete_contact = input("Input FIRST NAME and SURNAME ( or PHONE NUMBER) of the contact with you want to delete > ")
    for row in read_file():
        if f'{row[0]} {row[1]}' == delete_contact or row[2] == delete_contact:
            print('Note deleted')
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
    header = ['Name', 'Surname', 'Phone number', 'Email Address', 'Birthday']
    main_menu()
