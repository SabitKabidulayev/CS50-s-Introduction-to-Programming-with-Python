name = input("What's you name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")