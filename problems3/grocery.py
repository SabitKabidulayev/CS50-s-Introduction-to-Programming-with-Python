def main():
    my_grocery = grocery()
    keys_sorted = sorted(my_grocery.keys())
    for k in keys_sorted:
        print(f"{my_grocery[k]} {k}")

def grocery():
    grocery_list = {}
    while True:
        try:
            item = input().strip().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            return grocery_list

main()