def main():
    percent = convert(input("Fraction: "))
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            xy = fraction.strip().split("/")
            x = int(xy[0])
            y = int(xy[1])
            if x<=y:
                return round(x/y * 100)
            if y == 0:
                raise ZeroDivisionError
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
