def main():
    user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    input_formatted = user_input.lower().strip()
    if forty_two(input_formatted):
        print("Yes")
    else:
        print("No")

def forty_two(answer):
    match answer:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False

main()