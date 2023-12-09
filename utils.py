import os
import sys


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def clear_input_buffer():
    if os.name == "nt":
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        sys.stdin.read()


def load_file(path):
    with open(path, "r") as file:
        return file.read().splitlines()


