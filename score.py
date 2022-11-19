import random


def main():
    score = float(input("Enter score: "))
    print(determine_status(score,))
    random_score = determine_randon()
    print(f"{random_score}\n{determine_status(random_score)}")


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def determine_randon():
    randon_score = random.randint(0, 100)
    return randon_score

main()
