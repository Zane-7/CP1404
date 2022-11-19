import random


def main():
    get_menu()
    choice = input(">>> ").upper()
    score = []
    while choice != "Q":
        if choice == "G":
            score = determine_randon()
            print(score)
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        get_menu()
        choice = input(">>> ").upper()
    print("farewell.")


def get_menu():
    print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")


def determine_randon():
    return random.randint(0, 100)


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * score)


main()
