def main():
    user_input = input("Greeting: ")
    input_formatted = user_input.strip()
    print(greeting_evaluation(input_formatted))

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()
