from random import randint


def check_secret_number(guess, secret):
    if guess > secret:
        print "Sorry, that's not the number. Try something smaller"
        return False

    elif guess < secret:
        print "Sorry, that's not the number. Try something bigger"
        return False
    else:
        print "Congrats! the number was {}".format(secret)
        return True


def main():
    secret = randint(1, 100)
    found = False

    while not found:
        guess = int(raw_input("Guess the secret number (between 1 and 100): "))
        found = check_secret_number(guess, secret)


if __name__ == '__main__':
    main()
