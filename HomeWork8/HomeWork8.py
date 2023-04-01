import csv
import codecs
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def menu():
    while True:
        print("/==============================/")
        print('Select an option:')
        print('1. Add a contact')
        print('2. Search for a contact')
        print('3. Remove contact')
        print('4. Show all contacts')
        print('5. Exit')
        option = input()
        if option == '1':
            add_contact()
        elif option == '2':
            search_contacts()
        elif option == '3':
            remove_contact_from_file(input("Введите контакт для удаления: "))
        elif option == '4':
            print(show_info())
        elif option == '5':
            break
        else:
            print('Invalid option')


def show_info():
    with open('data.txt', 'r', encoding='utf-8') as file:
        phonebook = file.read().split('\n')
    return phonebook


def add_contact() -> str:
    name = input("Введите контакт для добавления: ")
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{name}')


def remove_contact_from_file(name):
    with open('data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('data.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
    return f'{name} has been deleted from data.txt'


def search_contacts():
    with open('data.txt', 'r', encoding='utf-8') as file:
        phonebook = file.read().split('\n')
        temp = input("Введите критерий поиска: ")
        for i in phonebook:
            if temp in i:
                print(i)


menu()