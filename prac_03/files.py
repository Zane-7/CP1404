# program 1：
out_file = open("name.txt", "w")
name = input("Please enter your name:")
print(name, file=out_file)
out_file.close()


# program 2：
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")


# program 3:
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)


# program 4:
in_file = open("numbers.txt", "r")
total_line = 0
for line in in_file:
    number = int(line)
    total_line += 1
in_file.close()
print(f"{total_line}")