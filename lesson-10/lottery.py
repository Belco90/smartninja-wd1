from random import randint


def generate_random(numbers):
    new_number = randint(1, 99)

    if new_number not in numbers:
        numbers.append(new_number)


def main():
    print "Welcome to the Lottery numbers generator."
    count = int(raw_input("Please enter how many random numbers would you like to have: "))

    numbers = []
    while len(numbers) < count:
        generate_random(numbers)

    print numbers


if __name__ == '__main__':
    main()
