def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_with_2_letters(s) and correct_len(s) and correct_num(s) and s.isalnum():
        return True
    else:
        return False

def start_with_2_letters(s):
    try:
        if s[0].isalpha() == True and s[1].isalpha() == True:
            return True
        else:
            return False
    except IndexError:
        pass


def correct_len(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def correct_num(s):
    for i in range(len(s)-1):
        if s[i].isdigit() and not s[i+1].isdigit():
            return False
        elif s[i].isalpha() and s[i+1] == "0":
            return False
    return True


if __name__ == "__main__":
    main()
