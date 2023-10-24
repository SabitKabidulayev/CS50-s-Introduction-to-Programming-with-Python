def main ():
    input_str=input("Enter your string: ")
    print(convert(input_str))


def convert (emoticons):
    return emoticons.replace(":)","🙂").replace(":(","🙁")

main()