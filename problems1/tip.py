def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.removeprefix("$"))


def percent_to_float(p):
    percent_string = p.removesuffix("%")
    percent_float = float(percent_string)
    return percent_float / 100


main()