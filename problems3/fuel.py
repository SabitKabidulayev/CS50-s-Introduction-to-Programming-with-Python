def main():
    percent = get_percentage("Fraction: ")
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

def get_percentage(prompt):
    while True:
        try:
            xy = input(prompt).strip().split("/")
            x = int(xy[0])
            y = int(xy[1])
            if x<=y:
                return round(x/y * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()
