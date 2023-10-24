x = float(input("What's x? "))
y = float(input("What's y? "))

# round(number[, ndigits])
z = x / y
print(f"{z:.2f}")

z = round(x / y, 2)
print(f"{z:,}")
print(z)


