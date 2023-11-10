from game import game_loop
from leaderboards import show_leaderboard
from utils import *


def main_menu():
    print(
        f"""
████████╗██╗   ██╗██████╗ ███████╗██████╗ 
╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
   ██║    ╚████╔╝ ██████╔╝█████╗  ██████╔╝
   ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗
   ██║      ██║   ██║     ███████╗██║  ██║
   ╚═╝      ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝

[1] Play Game
[2] Leaderboards
[3] Exit
"""
    )

    return input("Enter option: ")


def main():
    clear_terminal()

    score = 0

    while True:
        clear_terminal()
        choice = main_menu()
        match choice:
            case "1":
                score += game_loop()
                print(score)
            case "2":
                show_leaderboard()
            case "3":
                print("Thanks for playing!")
                exit()
            case _:
                print("Invalid choice. Try again.")
                break


if __name__ == "__main__":
    main()
