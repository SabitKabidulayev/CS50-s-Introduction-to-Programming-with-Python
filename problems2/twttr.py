def main():
    input_s = input("Input: ").strip()
    print(ommit_vowels(input_s))

def ommit_vowels(s):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for vowel in vowels:
        s = s.replace(vowel, "")
    return s

main()