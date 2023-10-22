def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")
    print(float(interpreter(x, y, z)))

def interpreter (num1, operator, num2):
    n1 = int(num1)
    n2 = int(num2)
    match operator:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            if n2 == 0:
                return "Can't divide by 0"
            else:
                return n1 / n2

main()