import pyinputplus as pyip

valid_operations = ["+", "-", "*", "x", "/", "%", "exit"]


def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        print("Never divide by zero worst mistake of my life")
        exit(1)

    else:
        return a / b


def modulo(a, b):
    if b == 0:
        print("Never divide by zero worst mistake of my life")
        exit(1)

    else:
        return a % b


def main():
    try:
        operation = pyip.inputChoice(valid_operations)
        if operation.lower() == "exit":
            exit()

        num1 = pyip.inputFloat("Enter the first number: ")
        num2 = pyip.inputFloat("Enter the second number: ")
        available = {
            "+": addition,
            "-": substraction,
            "*": multiplication,
            "x": multiplication,
            "/": division,
            "%": modulo
        }
        result = available[operation](num1, num2)
        print(result)

    except KeyboardInterrupt:
        print("Goodbye")


if __name__ == "__main__":
    main()