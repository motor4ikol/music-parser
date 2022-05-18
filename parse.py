import csv

import os

from colorama import init, Fore

from config import out_folder, name, debug


init()


def debug_print(debug_text):
    if debug: print(Fore.CYAN + "DEBUG: " + Fore.YELLOW + str(debug_text) + "\n", Fore.RED + 100 * "-", Fore.RESET)


def parse(f_name):
    with open(f_name + ".txt", encoding="utf-8") as file:
        t = file.read()
    ls = t.split("\n")

    for i in range(len(ls)):
        ls[i] = ls[i].split(" - ", 1)
    print(Fore.GREEN + "Parsing done! \n", Fore.RED + 100 * "-")
    debug_print(ls)

    return ls


def writer(list, f_name=name):
    with open(out_folder + "\\" + f_name + ".csv") as f:
        reader = csv.reader(f)
    debug_print(reader)


if not os.path.exists(out_folder):
    os.mkdir(out_folder)

writer(parse(name))
