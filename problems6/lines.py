import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py") == False:
        sys.exit("Not a python file")

    filename = sys.argv[1]
    n = 0
    try:
        with open(filename) as file:
            for line in file:
                if line.strip() == "":
                    continue
                elif line.strip().startswith("#") == True:
                    continue
                else:
                    n += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(n)

if __name__ == "__main__":
    main()