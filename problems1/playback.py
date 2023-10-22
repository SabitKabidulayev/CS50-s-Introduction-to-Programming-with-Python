def main():
    input_str=input("Enter your string: ")
    print(playback(input_str))

def playback(normal_speed):
    return normal_speed.replace(" ", "...")

main()