import emoji

def main():
    code = input("Input: ")
    result = emoji.emojize(code, language="alias")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()