from utils import *


def show_leaderboard():
    clear_terminal()
    leaderboard = load_file("texts/leaderboard.txt")

    print(
        """
    __ _  _  __ _  _  _  _  _  _ 
|  |_ |_|| \|_ |_)|_)/ \|_||_)| \\
|__|__| ||_/|__| \|_)\_/| || \|_/
"""
    )

    print("Rank\t\tName\t\tTime\t\tScore")
    print("----\t\t----\t\t----\t\t-----")
    for index, item in enumerate(leaderboard):
        name, time, score = item.split(",")

        # names longer than 7 characters cause overflow,
        if len(name) > 7:
            name = f"{name[:5]}.."

        print(f"{index + 1}\t\t{name}\t\t{time}\t\t{score}")

    for i in range(len(leaderboard), 10):
        print(f"{i + 1}\t\t -\t\t0.0\t\t0")

    if len(leaderboard) == 0:
        print("\n  Looks like no one has played yet...")

    input("\nPress [ENTER] to go to Menu... ")


def insert_to_leaderboard(time, score):
    clear_terminal()

    leaderboard = load_file("texts/leaderboard.txt")

    entries = [item.split(",") for item in leaderboard]

    name = ""
    while name == "":
        name = input("Enter username: ")
        clear_terminal()

    for entry in entries:
        while name.lower() == entry[0].lower():
            clear_terminal()
            print("Username already in leaderboard.")
            name = input("Please enter a valid username: ")

    entries.append([name, str(time), str(score)])

    # sort the list based on its time and score
    # secondary sort: time
    # primary sort: score
    entries.sort(key=lambda entry: float(entry[1]))
    entries.sort(key=lambda entry: int(entry[2]), reverse=True)

    unique_entries = []
    for entry in entries:
        if entry not in unique_entries:
            unique_entries.append(entry)

    with open("texts/leaderboard.txt", "w") as file:
        file.write(
            "\n".join(
                ",".join(str(word) for word in entry) for entry in unique_entries[:10]
            )
        )


def show_code_leaderboard():
    clear_terminal()
    leaderboard = load_file("texts/code_leaderboard.txt")

    print(
        """
    __ _  _  __ _  _  _  _  _  _ 
|  |_ |_|| \|_ |_)|_)/ \|_||_)| \\
|__|__| ||_/|__| \|_)\_/| || \|_/
"""
    )

    print("Rank\t\tName\t\tWPM\t\tAccuracy")
    print("----\t\t----\t\t----\t\t-------")
    for index, item in enumerate(leaderboard):
        name, wpm, accuracy = item.split(",")

        if len(name) > 7:
            name = f"{name[:5]}.."

        print(f"{index + 1}\t\t{name}\t\t{wpm}\t\t{float(accuracy) * 100:.2f}%")

    for i in range(len(leaderboard), 10):
        print(f"{i + 1}\t\t -\t\t-\t\t-")

    if len(leaderboard) == 0:
        print("\n  Looks like no one has played yet...")

    input("\nPress [ENTER] to go to Menu... ")


def insert_to_code_leaderboard(wpm, accuracy):
    clear_terminal()

    leaderboard = load_file("texts/code_leaderboard.txt")

    entries = [item.split(",") for item in leaderboard]

    name = ""
    while name == "":
        name = input("Enter username: ")
        clear_terminal()

    for entry in entries:
        while name.lower() == entry[0].lower():
            clear_terminal()
            print("Username already in leaderboard.")
            name = input("Please enter a valid username: ")

    entries.append([name, str(wpm), str(accuracy)])
    entries.sort(key=lambda entry: float(entry[1]), reverse=True)

    unique_entries = []
    for entry in entries:
        if entry not in unique_entries:
            unique_entries.append(entry)

    with open("texts/code_leaderboard.txt", "w") as file:
        file.write(
            "\n".join(
                ",".join(str(word) for word in entry) for entry in unique_entries[:10]
            )
        )
