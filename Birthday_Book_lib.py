# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

import datetime
import os

date_time = datetime.datetime.now()


def log(msg):
    with open("Birthday_Book.log", "a") as file:
        message = date_time.strftime("%Y-%m-%d %H:%M") + " : " + msg + "\n"
        file.write(message)


def import_from_file(birthday_book):
    if os.path.exists("Birthday_Book.csv"):
        with open("Birthday_Book.csv", "r") as file:
            lines = file.readlines()
            for line in lines:
                elements = line.split(";")
                name = elements[0]
                day = elements[1]
                month = elements[2]
                year = elements[3]
                value = list()
                value.append(day)
                value.append(month)
                value.append(year)
                birthday_book[name] = value
        log("Импорт из файла")
    else:
        log("Файл для импорта не найден")


def welcome():
    print("*******")
    print("*** BirthdayBook - справочник дней рождения ***")
    print("*******")
    log("Программа запустилась")


def menu():
    print("=== === ===")
    print("Режимы работы:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Сохранить в файл")
    print("6. Очищение всего справочника")
    print("0. Выход")


def input_data():
    temp = list()
    day = input("Введите день: ")
    month = input("Введите месяц: ")
    year = input("Введите год: ")
    temp.append(day)
    temp.append(year)
    temp.append(month)
    return temp


def show(birthday_book):
    if len(birthday_book) == 0:
        print("# Телефонный справочник пуст #")
    else:
        print("--- Телефонный справочник ---")
        for tel in birthday_book:
            value = birthday_book[tel]
            temp = value[0] + " " + value[1] + " " + value[2] + ", " + value[3]
            print(name, ':', temp)
        print("--- --- ---")
        log("Вывод справочника на экран")


def input_record(birthday_book):
    name = input("Введите номер телефона: ")
    if name in birthday_book:
        print("# Такой номер уже существует #")
        log("Неудачная попытка добавления записи с номером " + name)
    else:
        value = input_data()
        birthday_book[tel] = value
        print("# Запись успешно добавлена #")
        log("Запись с " + tel + " успешно добавлена")


def edit_record(phone_book):
    name = input("Введите номер телефона: ")
    if name in phone_book:
        temp = input_data()
        birthday_book[tel] = temp
        print("# Запись успешно изменена #")
        log("Запись с " + name + " успешно изменена")
    else:
        print("# Вы ввели неправильный номер #")
        log("Неудачная попытка редактирования записи с номером " + name)


def delete_record(birthday_book):
    tel = input("Введите номер телефона для удаления: ")
    if tel in birthday_book:
        birthday_book.pop(tel)
        print("# Запись " + name + " удалена #")
        log("Запись с " + name + " успешно удалена")
    else:
        print("# Вы ввели неправильный номер #")
        log("Неудачная попытка удаления записи с номером " + name)


def export_to_file(birthday_book):
    with open("Birthday_Book.csv", "w") as file:
        for name in birthday_book:
            value = birthday_book[tel]
            temp = name + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + value[3] + "\n"
            file.write(temp)
    log("Экспорт в файл")