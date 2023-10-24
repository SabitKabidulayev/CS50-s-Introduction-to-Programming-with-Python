def main():
    mass=int(input("Enter mass: "))
    print(calculate_energy(mass))

def calculate_energy(m):
    return m * 300000000**2

main()