import time
import random

from utils import *
from leaderboards import *


def get_random(texts):
    return texts.pop(texts.index(random.choice(texts)))


def get_texts(path, word_freq):
    selected_texts = set()
    texts = load_file(path)

    for _ in range(word_freq):
        text = get_random(texts)
        selected_texts.add(text)

    return list(selected_texts)


def instructions(progammer_mode=False):
    print(
        f"""
___    _____ _     ________ _     __
 | |\|(_  | |_)| |/   |  | / \|\|(_ 
_|_| |__) | | \|_|\__ | _|_\_/| |__)
    
  Type the {'code statements' if progammer_mode else 'words'} that will be shown to you as fast as you can!
        """
    )

    start_confirm = input("  Are you ready? [Y/N]:  ").upper()
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
██████╔╝██╗██╗██╗
╚═════╝ ╚═╝╚═╝╚═╝
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
███████╗██╗██╗██╗
╚══════╝╚═╝╚═╝╚═╝
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
 ██║██╗██╗██╗
 ╚═╝╚═╝╚═╝╚═╝
        """
    )
    time.sleep(1)
    clear_terminal()
    return


def show_text(text):
    clear_terminal()

    spaces = 25 if len(text) <= 5 else len(text) + 5
    print("=" * (spaces + 2))
    print(f"|{' ' * spaces}|")
    print(f"|{text : ^{spaces}}|")
    print(f"|{' ' * spaces}|")
    print("=" * (spaces + 2))


def show_mistyped_texts(words):
    clear_terminal()
    print(
        """
   ___ _____\ / _  __ _        _  _  _  __
|V| | (_  |  Y |_)|_ | \   | |/ \|_)| \(_ 
| |_|___) |  | |  |__|_/   |^|\_/| \|_/__)
"""
    )
    print("ACTUAL\t\t\tTYPED")

    for word in words:
        print(f"{word[0]}\t\t\t{word[1]}")

    print("===========================")
    input("\nPress [ENTER] to continue... ")


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


def normal_mode():
    clear_terminal()

    if not instructions():
        return

    timer()

    words = (
        get_texts("texts/three_letter.txt", 15)
        + get_texts("texts/four_letter.txt", 15)
        + get_texts("texts/five_letter.txt", 15)
    )

    score_system = {3: 2, 4: 5, 5: 7}
    mistyped_words = []
    total_score = 0

    start_time = time.time()
    while len(words) > 0:
        word = get_random(words).lower()
        show_text(word)

        typed_word = input("Enter word: ")

        if typed_word == word:
            total_score += score_system[len(word)]
        else:
            mistyped_words.append([word, typed_word])

    time_passed = round(time.time() - start_time, 2)

    game_over()

    clear_terminal()
    print(f"You scored {total_score} points in {time_passed} seconds!")
    time.sleep(3)

    clear_input_buffer()
    show_mistyped_texts(mistyped_words)

    insert_to_leaderboard(time_passed, total_score)
    show_leaderboard()

    input("\nPress [ENTER] to continue... ")


def programmer_mode():
    clear_terminal()

    if not instructions(True):
        return

    timer()

    lines = get_texts("texts/code_lines.txt", 5)

    mistyped_chars = 0
    typed_chars = 0
    total_characters = 0

    start_time = time.time()
    while len(lines) > 0:
        line = get_random(lines)
        total_characters += len(line)

        show_text(line)

        typed_line = input("Enter word: ")
        typed_chars += len(typed_line)
        mistyped_chars += len(line)

        if typed_line != line:
            for chr in typed_line:
                iter_count = 0
                for letter in line:
                    iter_count += 1
                    if chr == letter or iter_count == 3:
                        mistyped_chars -= 1
                        line = line[line.index(letter) + 1 :]
                        break
        else:
            mistyped_chars -= len(line)

    time_passed = round(time.time() - start_time, 2)

    game_over()

    accuracy = (total_characters - mistyped_chars) / total_characters
    lines_per_minute = max(0, ((typed_chars / 5) - mistyped_chars) / (time_passed / 60))

    clear_terminal()
    clear_input_buffer()

    print(
        f"You typed {lines_per_minute:.2f} WPM with an accuracy rating of {(accuracy * 100):.2f}%..."
    )
    input("\nPress [ENTER] to continue... ")

    insert_to_code_leaderboard(round(lines_per_minute, 2), round(accuracy, 2))
    show_code_leaderboard()

    input("\nPress [ENTER] to continue... ")
