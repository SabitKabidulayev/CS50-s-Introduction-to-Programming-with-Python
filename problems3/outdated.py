def main():
    month, day, year = input_date("Date: ")
    print(f"{year:04}", f"{month:02}", f"{day:02}", sep="-")

def input_date(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input(prompt).strip()
            if date[0].isalpha():
                m, d, y = date.split(" ")
                d = d[0:len(d)-1]
                m = months.index(m) + 1
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31 and int(y) > 0:
                    return int(m), int(d), int(y)
            elif date[0].isdigit():
                m, d, y = date.split("/")
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31 and int(y) > 0:
                    return int(m), int(d), int(y)
            else:
                continue
        except ValueError:
            pass

main()


