import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                second, first = row["name"].split(", ")
                students.append({"first": first, "last": second, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]} file")

    with open(sys.argv[2], "w") as file:
       writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
       writer.writeheader()
       for student in students:
           writer.writerow(student)

if __name__ == "__main__":
    main()