def main():
    camelCase = input("camelCase: ").strip()
    snake_case(camelCase)

def snake_case(s):
    for c in s:
        if c.islower():
            print(c, end="")
        elif c.isupper():
            print("_", c.lower(), sep="", end="")
    print()

main()