MINIMUM_LENGTH = 6


def main():
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(MINIMUM_LENGTH):
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password too short!")
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    return password


def print_stars(sequence):
    print("*" * len(sequence))


main()
