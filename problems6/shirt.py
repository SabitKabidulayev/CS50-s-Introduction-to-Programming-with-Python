import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    _ , ext1 = os.path.splitext(sys.argv[1])
    _ , ext2 = os.path.splitext(sys.argv[2])

    extensions = [".jpg", ".jpeg", ".png"]

    if ext1.lower() not in extensions:
        sys.exit("Invalid input")

    if ext2.lower() not in extensions:
        sys.exit("Invalid output")

    if ext1.lower() != ext2.lower():
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        result = ImageOps.fit(image, size)
        result.paste(shirt, shirt)
        result.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()