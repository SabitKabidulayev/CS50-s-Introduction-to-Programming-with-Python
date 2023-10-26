import random

def main():
    level = get_int("Level: ")
    num = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")
        if guess < num:
            print("Too small!")
        if guess > num:
            print("Too large!")
        if guess == num:
            print("Just right!")
            break

def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass

if __name__ == "__main__":
    main()