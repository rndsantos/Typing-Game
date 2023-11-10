import time
import random

from utils import *


def get_random_word(words):
    return words.pop(words.index(random.choice(words)))


def instructions():
    print(
        """
INSTRUCTIONS: Type the word that will be shown to you as fast as you can!
              You will be typing 45 words total.
        """
    )

    start_confirm = input("Are you ready? [Y/N]:  ").upper()
    clear_terminal()

    if start_confirm == "Y":
        return True

    return False


def timer():
    print(
        """
██████╗ 
╚════██╗
 █████╔╝
 ╚═══██╗
██████╔╝
╚═════╝ 
        """
    )
    time.sleep(1)
    clear_terminal()
    print(
        """
██████╗ 
╚════██╗
 █████╔╝
██╔═══╝ 
███████╗
╚══════╝
        """
    )
    time.sleep(1)
    clear_terminal()
    print(
        """
 ██╗
███║
╚██║
 ██║
 ██║
 ╚═╝
        """
    )
    time.sleep(1)
    clear_terminal()
    return


def show_word(word):
    clear_terminal()
    print("===========================")
    print(f"|{' ' * 25}|")
    print(f"|{word : ^25}|")
    print(f"|{' ' * 25}|")
    print("===========================")


def game_loop():
    clear_terminal()    

    if not instructions():
        return

    timer()

    words = load_file("words.txt")
    score_system = {3: 1, 4: 3, 5: 5}
    total_score = 0
    
    while len(words) > 0:
        word = get_random_word(words).lower()
        typed_word = ""

        while typed_word != word:
            show_word(word)
            typed_word = input("Enter word: ")

        total_score += score_system[len(word)]

    return total_score
