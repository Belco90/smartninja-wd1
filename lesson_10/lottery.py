from random import randint


def generate_unique_random_numbers(count):
    numbers = []
    while len(numbers) < count:

        new_number = randint(1, 99)

        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def main():
    print "Welcome to the Lottery numbers generator."
    count = int(raw_input("Please enter how many random numbers would you like to have: "))

    numbers = generate_unique_random_numbers(count)

    print numbers


if __name__ == '__main__':
    main()
