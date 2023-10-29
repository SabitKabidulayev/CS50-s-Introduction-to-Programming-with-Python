def main():
    s = input("Input: ").strip()
    print(shorten(s))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()
