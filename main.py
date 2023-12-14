# AUTHOR: Roberto Neil Santos
# SECTION: B-5L
# COMPLETION DATE: 12-10-23
# TYPING GAME: TIPO

from game import normal_mode, programmer_mode
from leaderboards import show_leaderboard, show_code_leaderboard
from utils import *


def main_menu():
    print(
        f"""
▄▄▄▄▄▄▪   ▄▄▄·      
▀•██ ▀██ ▐█ ▄█ ▄█▀▄ 
  ▐█.▪▐█· ██▀·▐█▌.▐▌
  ▐█▌·▐█▌▐█▪·•▐█▌.▐▌
  ▀▀▀ ▀▀▀.▀    ▀█▄▀▪

  [1] Play Game
  [2] Leaderboards
  
  [0] Exit
"""
    )

    return input("Enter option: ")


def game_menu():
    clear_terminal()
    print(
        f"""
 ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .    • ▌ ▄ ·.       ·▄▄▄▄  ▄▄▄ .
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ·██ ▐███▪▪     ██▪ ██ ▀▄.▀·
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄    ▐█ ▌▐▌▐█· ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄
▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ██ ██▌▐█▌▐█▌.▐▌██. ██ ▐█▄▄▌
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀     ▀▀  █▪▀▀▀ ▀█▄▀▪▀▀▀▀▀•  ▀▀▀ 

  [1] Normal Mode
  [2] Programmer Mode

  [0] Back
"""
    )

    match input("Enter option: "):
        case "1":
            normal_mode()
        case "2":
            programmer_mode()
        case "0":
            main()
        case _:
            game_menu()


def leaderboard_menu():
    clear_terminal()
    print(
        f"""
▄▄▌  ▄▄▄ . ▄▄▄· ·▄▄▄▄  ▄▄▄ .▄▄▄  ▄▄▄▄·        ▄▄▄· ▄▄▄  ·▄▄▄▄  .▄▄ · 
██•  ▀▄.▀·▐█ ▀█ ██▪ ██ ▀▄.▀·▀▄ █·▐█ ▀█▪▪     ▐█ ▀█ ▀▄ █·██▪ ██ ▐█ ▀. 
██▪  ▐▀▀▪▄▄█▀▀█ ▐█· ▐█▌▐▀▀▪▄▐▀▀▄ ▐█▀▀█▄ ▄█▀▄ ▄█▀▀█ ▐▀▀▄ ▐█· ▐█▌▄▀▀▀█▄
▐█▌▐▌▐█▄▄▌▐█ ▪▐▌██. ██ ▐█▄▄▌▐█•█▌██▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█•█▌██. ██ ▐█▄▪▐█
.▀▀▀  ▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀·▀▀▀▀  ▀█▄▀▪ ▀  ▀ .▀  ▀▀▀▀▀▀•  ▀▀▀▀ 

  [1] Normal Mode
  [2] Programmer Mode

  [0] Back
"""
    )

    match input("Enter option: "):
        case "1":
            show_leaderboard()
        case "2":
            show_code_leaderboard()
        case "0":
            main()
        case _:
            leaderboard_menu()


def main():
    clear_terminal()

    while True:
        clear_terminal()
        choice = main_menu()
        match choice:
            case "1":
                game_menu()
            case "2":
                leaderboard_menu()
            case "0":
                print("Thanks for playing!")
                exit()


main()
