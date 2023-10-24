def main():
    user_time = input("What time is it? ").strip()
    converted_time = convert(user_time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
        return
    elif 12 <= converted_time <= 13:
        print("lunch time")
        return
    elif 18 <= converted_time <= 19:
        print("dinner time")
        return
    else:
        return

def convert(time):
    if time.endswith(" a.m."):
        hours, minutes = time.removesuffix(" a.m.").split(":")
        if hours == "12":
            return 0
        else:
            return float(int(hours) + int(minutes)/60)
    elif time.endswith(" p.m."):
        hours_pm, minutes = time.removesuffix(" p.m.").split(":")
        if hours_pm != "12":
            hours = 12 + int(hours_pm)
        else:
            hours = 12
        return float(int(hours) + int(minutes)/60)
    else:
        hours, minutes = time.split(":")
        return float(int(hours) + int(minutes)/60)

if __name__ == "__main__":
    main()
