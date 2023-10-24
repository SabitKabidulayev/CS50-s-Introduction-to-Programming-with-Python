def main():
    change_owed = coke_machine()
    print(f"Change Owed: {change_owed}")

def coke_machine():
    coke_price = 50
    while True:
        n = int(input("Insert Coin: "))
        print(f"Amount Due: {coke_price}")
        if n == 5 or n == 10 or n == 25:
            coke_price -= n
            print(f"Amount Due: {coke_price}")
            if coke_price <= 0:
                return -coke_price

main()