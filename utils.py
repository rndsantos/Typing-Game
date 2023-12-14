import os
import sys
import random


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def clear_input_buffer():
    """Flushes the input stream

    After the game has ended, there is a tendency that thre are leftover
    inputs by the player causing the next inputs to be filled out.
    To avoid such problem, flushing the input is necessary.
    """

    if os.name == "nt":
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def load_file(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.read().splitlines()

    return []


def get_random(texts):
    """Gets a random element from texts and removes said element from texts"""

    return texts.pop(texts.index(random.choice(texts)))


def get_texts(path, word_count):
    """Gets N random words or texts from text file

    Parameters
    ----------
    path : str
        The file location of text
    word_count : int
        Number of words or texts to get

    Returns
    -------
    list
    """

    selected_texts = set()
    texts = load_file(path)

    for _ in range(word_count):
        text = get_random(texts)
        selected_texts.add(text)

    return list(selected_texts)


def get_errors(text, typed_text):
    """Gets type errors by the user

    Parameters
    ----------
    text : str
        The base text
    typed_text : str
        The text that the user typed

    Returns
    -------
    int
    """

    # how far to look for the typed letter in the remaining text
    # too far of a match will be considered an error
    CHECK_THRESHOLD = 3
    mistyped_characters = max(len(text), len(typed_text))

    if typed_text == text:
        return 0

    if typed_text == "":
        return mistyped_characters

    # check if there is a match for every typed character in the base text,
    # then subtract that letter from the mistyped_characters
    for typed_character in typed_text:
        for character in text:
            # there are some cases where the player skips a few letters
            # to track that, check if the letter is found within the remaining text,
            # if it is found and within the CHECK_THRESHOLD, skip the passed text and
            # continue checking starting with the found letter
            found = text.find(typed_character)
            if typed_character == character or (
                found < CHECK_THRESHOLD and found != -1
            ):
                mistyped_characters -= 1

                # cuts off already checked characters
                text = text[text.index(character) + 1 :]
                break

            break

    return mistyped_characters


def get_acccuracy(total_characters, mistyped_characters):
    return (total_characters - mistyped_characters) / total_characters


def get_wpm(typed_characters, mistyped_characters, time_passed):
    """Gets words per minute of player

    There is a tendency where erorrs are greater than the typed characters
    causing a negative WPM. If that happens, just set the WPM to 0.

    The expression 'type_characters / 5' are the total number of words typed

    Parameters
    ----------
    typed_characters : int
        Number of characters typed by the player
    mistyped_characters : int
        Number of errors made by the player
    time_passed : float
        Time took to finish the game

    Returns
    -------
    float
    """

    return max(0, ((typed_characters / 5) - mistyped_characters) / (time_passed / 60))
