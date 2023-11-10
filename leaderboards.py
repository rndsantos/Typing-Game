from utils import *


def show_leaderboard():
    leaderboard = load_file("leaderboard.txt")

    print("Name\t\tScore")
    for item in leaderboard:
        name, score = item.split(",")
        print(f"{name}\t\t{score}")


def insert_to_leaderboard(name, score):
    leaderboard = load_file("leaderboard.txt")
    with open("leaderboard.txt", "w") as file:
        pass


show_leaderboard()
