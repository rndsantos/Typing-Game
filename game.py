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


def show_mistyped_words(words):
    print("===========================")
    print("M I S T Y P E D   W O R D S")
    print("ACTUAL\t\t\tTYPED")

    for word in words:
        print(f"{word[0]}\t\t\t{word[1]}")

    print("===========================")

    time.sleep(3)


def show_score(score, time_passed):
    clear_terminal()
    print(f"You scored {score} points in {time_passed} seconds!")
    time.sleep(3)


def game_over():
    print(
        """
 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                 
""",
        end="\t",
    )
    time.sleep(1)
    print(
        """
 ██████╗ ██╗   ██╗███████╗██████╗ 
██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                   
"""
    )

    time.sleep(3)


def game_loop():
    clear_terminal()

    if not instructions():
        return

    timer()

    words = load_file("words.txt")
    score_system = {3: 2, 4: 5, 5: 7}
    mistyped_words = []
    total_score = 0

    start_time = time.time()
    while len(words) > 0:
        word = get_random_word(words).lower()
        print(f"{len(words)} words left...")
        show_word(word)

        typed_word = input("Enter word: ")

        if typed_word == word:
            total_score += score_system[len(word)]
        else:
            mistyped_words.append([word, typed_word])

    time_passed = round(time.time() - start_time, 2)

    game_over()
    show_score(total_score, time_passed)
    show_mistyped_words(mistyped_words)

    input("\nPress enter to continue... ")

    return total_score
