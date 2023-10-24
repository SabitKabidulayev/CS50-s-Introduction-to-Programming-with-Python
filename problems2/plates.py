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
    for c in s[0:2]:
        if c.isalpha():
            return True
        else:
            return False

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

main()