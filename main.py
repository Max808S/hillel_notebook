from csv import DictWriter

import csv
import pandas as pd


def check_base():
    """
    При запуске программы проверяем есть ли ранее
    сохранённая база данных, и сообщаем о количестве записей в ней
    """
    try:
        df = pd.read_csv('userbase.csv', delimiter=',', encoding='cp1251')
        column_count = len(df.axes[0])
        print(f'Файл userbase найден. Количество записей: {str(column_count)} \n')
    except Exception as ex:
        print(f'{ex} \nФайл userbase не найден.')


def add_note():
    """
    Добавление новой записи
    """
    try:
        # список названий столбцов, упомянутых в csv файле
        headers_csv = ['First name', 'Last name', 'Phone number', 'Address', 'Birthday']

        print(f'Добавление пользователя в записную книгу.')
        # входные данных о пользователе
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        phone_number = input('Введите номер телефона: ')
        address = input('Введите адрес: ')
        birthday = input('Введите дату рождения: ')

        # данные присвоенные словарю
        note_dict = {'First name': first_name, 'Last name': last_name,
                     'Phone number': phone_number, 'Address': address, 'Birthday': birthday}

        # открываем CSV файл в режиме добавления (упоминается как 'a')
        with open('userbase.csv', 'a', newline='') as f_object:
            # передаём объект файла CSV функции 'DictWriter'
            writer_object = DictWriter(f_object, fieldnames=headers_csv)

            # условие от повторного написания названий столбцов
            if f_object.tell() == 0:
                writer_object.writeheader()

            # передаём данные из словаря в качестве аргумента функции 'writerow'
            writer_object.writerow(note_dict)
            f_object.close()

        print(f'Пользователь {first_name} {last_name} добавлен в таблицу.')
    except Exception as ex:
        print(ex)


def check_note():
    """
    Просмотр всех записей
    """
    try:
        # читаем CSV файл
        df = pd.read_csv('userbase.csv', delimiter=',', encoding='cp1251')
        print(f'\nЗаписная книжка Hillel: \n\n{df}')
    except Exception as ex:
        print(f'{ex} \nЧто бы создать файл userbase, в главном меню нажмите [1]')


def edit_note():
    """
    Редактирование записи
    """
    try:
        # поиск и удаление
        del_note()
        # запись новых данных
        add_note()
    except Exception as ex:
        print(f'{ex} \nЧто бы создать файл userbase, в главном меню нажмите [1]')


def search_name():
    """
    Поиск в базе по имени, фамилии, номеру телефона
    """
    try:
        # читаем csv и делим строку ","
        csv_file = csv.reader(open('userbase.csv', "r"), delimiter=",")
        input_data = input('\nВведите имя, фамилию или номер телефона пользователя, '
                           'которого нужно найти: ')

        # цикл по списку csv
        data_value = False
        for row in csv_file:
            if input_data in row:
                data_value = True
            if data_value:
                print(row)
                break
        else:
            print(f'Запись {input_data} не найдена.')
    except Exception as ex:
        print(f'{ex} \nЧто бы создать файл userbase, в главном меню нажмите [1]')


def del_note():
    """
    Удаление записи из файла базы данных
    """
    try:
        with open('userbase.csv', 'r+') as in_file:
            del_data = input(f'\nВведите имя, фамилию или номер телефона пользователя, '
                             'которого нужно удалить: ')

            rows = [row for row in csv.reader(in_file) if del_data not in row]
            in_file.seek(0)
            in_file.truncate()
            writer = csv.writer(in_file)
            writer.writerows(rows)
            print(f'{del_data} и сопутствующие данные удалены.')
    except Exception as ex:
        print(f'{ex} \nЧто бы создать файл userbase, в главном меню нажмите [1]')


def sort(self=''):
    """
    Сортировка пользователей по имени или фамилии
    """
    try:
        df = pd.read_csv('userbase.csv', delimiter=',', encoding='cp1251')
        # self = имя или фамилия
        sort_res = df.sort_values(by=[self], ascending=True)
        print(f'\nЗаписная книжка Hillel: \n({self} сортировка) \n\n{sort_res}')
    except Exception as ex:
        print(f'{ex} \nЧто бы создать файл userbase, в главном меню нажмите [1]')


def cancel_menu():
    """
    Меню которое переводит пользователя в главное меню или завершение работы
    """
    print('\nПродолжить использовать приложение?')
    while True:
        a = int(input('Введи [1] что бы вернутся в меню или [2] что бы завершить работу: '))
        if a == 1:
            menu_interaction()
        elif a == 2:
            print('Hillel Notebook закрыт!')
            exit()
        else:
            print('Неверный ввод, попробуйте [1] или [2]')


def menu_interaction():
    """
    Главное меню программы
    """
    main_menu = 'Hillel Notebook' \
                '\n' \
                '\n[1] Добавить запись' \
                '\n[2] Посмотреть записи' \
                '\n[3] Изменить запись' \
                '\n[4] Удалить запись' \
                '\n[5] Поиск' \
                '\n[6] Сортировка' \
                '\n[7] Выход' \
                '\n'
    print(main_menu)

    while True:
        try:
            user_input = int(input('Главное меню [#]: '))
            if user_input == 7:
                print('Notebook закрыт!')
                exit()
            elif user_input == 1:
                add_note()
                cancel_menu()
            elif user_input == 2:
                check_note()
                cancel_menu()
            elif user_input == 3:
                edit_note()
                cancel_menu()
            elif user_input == 4:
                del_note()
                cancel_menu()
            elif user_input == 5:
                search_name()
                cancel_menu()
            elif user_input == 6:
                try:
                    df = pd.read_csv('userbase.csv', delimiter=',', encoding='cp1251')
                    while True:
                        user_sort_input = int(input('[1] Сортировка по имени  [2] Сорторовка по фамилии: '))
                        if user_sort_input == 1:
                            sort('First name')
                            cancel_menu()
                        elif user_sort_input == 2:
                            sort('Last name')
                            cancel_menu()
                        else:
                            print('Неверный ввод, попробуйте [1] или [2]')
                except Exception as ex:
                    print(f'{ex} \nИспользуйте [1] или [2] для выбора сортировки. \n')
            else:
                print('Неправильный ввод! Используйте [1] [2] [3] [4] [5] [6] [7] для навигации: ')
        except Exception as ex:
            print(f'{ex}\nНеправильный ввод! Используйте [1] [2] [3] [4] [5] [6] [7] для навигации: ')


if __name__ == '__main__':
    check_base()
    menu_interaction()
