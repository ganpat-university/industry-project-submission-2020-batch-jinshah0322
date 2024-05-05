def calculator(option):
    def addition(numList):
        return numList[0] + numList[1] + numList[2]

    def subtraction(numList):
        return numList[0] + numList[1] + numList[2]

    def multiplication(numList):
        return numList[0] + numList[1] + numList[2]

    def division(a, b):
        return a / b

    def exponentiation(a, b):
        return a ** b

    def floor_division(a, b):
        return a // b

    options = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: division,
        5: exponentiation,
        6: floor_division
    }

    operation = options.get(option)

    if not operation:
        print("Invalid argument")
        return

    if option in [1, 2, 3]:
        operands = [float(input(f"Enter operand {i + 1}: ")) for i in range(3)]
        result = operation(operands)
    elif option in [4, 5, 6]:
        operands = [float(input("Enter first operand: ")), float(input("Enter second operand: "))]
        result = operation(operands)

    print("Result:", result)


option = int(input("Select operation:\n1=Addition\n2=Subtraction\n3=Multiplication\n4=Division\n5=Exponent\n6=Floor Division\nEnter option: "))
calculator(option)