def main():
    user_input = input("Greeting: ")
    input_formatted = user_input.lower().strip()
    print(greeting_evaluation(input_formatted))

def greeting_evaluation(greeting):
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return "$0"
        else:
            return "$20"
    else:
        return "$100"

main()