from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
            sys.exit("Invalid usage")

    if len(sys.argv) != 1:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invlaid usage")

        if sys.argv[2] not in fonts:
            sys.exit("Invlaid usage")

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
        text = input("Input: ")
        print(figlet.renderText(text))
        return

    if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        text = input("Input: ")
        print(figlet.renderText(text))
        return

main()







