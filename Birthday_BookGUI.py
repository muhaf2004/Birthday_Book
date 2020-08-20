from tkinter import *
import os

birthday_book = dict()


def clear():
    input_name.delete(0, END)
    input_day.delete(0, END)
    input_month.delete(0, END)
    input_year.delete(0, END)


def add():
    name = input_name.get()
    if name in birthday_book:
        label_info.config(text="Такой день рождения уже существует")
    else:
        value = list()
        value.append(input_day.get())
        value.append(input_month.get())
        value.append(input_year.get())
        birthday_book[name] = value

        list_name.insert(END, name)


def select_list_tel(event):
    w = event.widget
    i = int(w.curselection()[0])
    name = w.get(i)

    value = birthday_book[name]
    day = value[0]
    month = value[1]
    year = value[2]

    clear()
    input_name.insert(0, name)
    input_day.insert(0, day)
    input_month.insert(0, month)
    input_year.insert(0, year)


window = Tk()
window.title("PhoneBook")
window.geometry("500x250")

# Объявление элементов окна
label_name = Label(text="Номер телефона")
input_name = Entry()

label_day = Label(text="Фамилия")
input_day = Entry()

label_month = Label(text="Имя")
input_month = Entry()

label_year = Label(text="Отчество")
input_year = Entry()

button_add = Button(text="Добавить", command=add)
button_clear = Button(text="Очистить", command=clear)

label_list_name = Label(text="Список телефонов")
list_name = Listbox()

label_info = Label(text="Программа готова к работе")

# Позиционирование
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_name.grid(row=0, column=1)

label_day.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_day.grid(row=1, column=1, padx=10)

label_month.grid(row=2, column=0, padx=10, pady=5, sticky="w")
input_month.grid(row=2, column=1)

label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
input_year.grid(row=3, column=1, padx=10)


button_add.grid(row=1, column=2, padx=10)
button_clear.grid(row=3, column=2, padx=10)

label_list_name.grid(row=0, column=3)
list_name.grid(row=1, column=3, rowspan=4, pady=15)

label_info.grid(row=5, column=0, columnspan=4, sticky="w")

list_name.bind('<<ListboxSelect>>', select_list_name)

if os.path.exists("BirthdayBook.csv"):
    with open("BirthdayBook.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            els = line.split(";")
            name = els[0]
            day = els[1]
            month = els[2]
            year = els[3]
            value = list()
            value.append(day)
            value.append(month)
            value.append(year)
            birthday_book[name] = value
            list_name.insert(END, name)

window.mainloop()