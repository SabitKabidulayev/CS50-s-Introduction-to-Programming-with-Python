import random


def main():
    n = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        attempt = 0
        while True:
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input())
                attempt += 1
                if answer == x + y:
                    score += 1
                    break
                if attempt == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
                if answer != x + y:
                    print("EEE")


            except ValueError:
                pass

    print(score)

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l == 1 or l == 2 or l == 3 :
                return l
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()