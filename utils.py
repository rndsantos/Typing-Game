import os

from sys import platform


def clear_terminal():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    else:
        os.system("cls")


def load_file(path):
    with open(path, "r") as file:
        return file.read().splitlines()
