valid_operations = ["+", "-", "*", "x", "/", "%", "exit"]

# Toutes les operations de calcul
def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Never divide by zero!!! Worst mistake of my life")
        exit(1)

    else:
        return a / b

def modulo(a, b):
    if b == 0:
        print("Never divide by zero!!! Worst mistake of my life")
        exit(1)

    else:
        return a % b

def num_validation():
    num1 = 0
    num2 = 0

    while True: # se relance automatiquement !
        try:
            num1 = float(input("Enter the first number: "))
            break # pour sortir de la boucle

        except ValueError:
            # si l'input n'est pas un nombre
            print("Not a number")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break

        except ValueError:
            print("Not a number")

    return num1, num2

# Menu
def main():
    while True:
        try:
            operation = input("Enter the operation sign you want to execute.\nType exit to quit.\n")

            # validation operateurs
            if operation.lower() not in valid_operations:
                print("Not a valid operation, try again!")
                print("Valid operators are: +, -, *, x, /, %")
                continue

            if operation.lower() == "exit":
                exit()

            num1, num2 = num_validation() # on exporte la validation pour eviter la redondance

            if operation == "+":
                # addition
                result = addition(num1, num2)

            elif operation == "-":
                # substract
                result = substraction(num1, num2)

            elif operation == "*" or operation.lower() == "x":
                # multiplication
                result = multiplication(num1, num2)

            elif operation == "/":
                # division
                result = division(num1, num2)

            elif operation == "%":
                # modulo
                result = modulo(num1, num2)

            print(result)

        except KeyboardInterrupt:
            # gestion d'erreurs
            print("Goodbye")
            exit()

# sans ces 2 lignes dessous, rien ne ce passe
if __name__ == "__main__":
    main()