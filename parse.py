import csv

import os

from colorama import init, Fore

from config import out_folder, name, debug

init()


def debug_print(debug_text):
    if debug:
        print(Fore.CYAN + "DEBUG: " + Fore.YELLOW + str(debug_text) + "\n", Fore.RED + 100 * "-", Fore.RESET)


def parse(f_name):
    with open(f_name + ".txt", encoding='utf-8') as file:
        t = file.read()
    ls = t.split("\n")

    for i in range(len(ls)):
        ls[i] = ls[i].split(" - ", 1)
    print(Fore.GREEN + "Parsing done! \n", Fore.RED + 100 * "-")
    debug_print(ls)

    return ls

def dict_gen(ls):
    dictio = []
    ls = [['Yellow Fire', 'Звёзды'], ['Melham_Music', 'Новое Поколение'], ['Yellow Fire, Лига кубизма', 'Этот новый год'], ['Yellow Fire', 'Я люблю майнкрафт'], ['Yellow Fire', 'Тотем бессмертия'], ['Yellow Fire', 'Будь тише'], ['Калимуллин Арслан', 'С эчпочмаками в зубах'], ['Yellow Fire, Матушка, Jack Looney', 'В незеритовой броне'], ['Yellow Fire', 'Лига кубизма'], ['Yellow Fire', 'Пчела упала'], ['Bav', 'ВУГЛУ'], ['kirkiimad', 'Майнкрафт'], ['Фикс', 'Кожаные штаны'], ['Арслан Калимуллин', 'Жёлтый персик'], ['Фиксай', 'Лук Батун'], ['Bav', 'Пчелобав урод'], ['Yellow Fire', 'Элитры']]
    for i in ls:
        dc = dict()
        dc["author"] = i[0]
        dc["song"] = i[1]
        dictio.append(dc)
    debug_print(dictio)
    return dictio

def writer(list, f_name=name):
    with open(out_folder + "\\" + f_name + ".csv") as f:
        writer = csv.writer(f)
    debug_print(writer)  # TODO: Добавить работу с csv


if not os.path.exists(out_folder):
    os.mkdir(out_folder)

writer(parse(name))
dict_gen([])
