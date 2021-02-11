import art


def check_the_continue_calculation(typing):
    """
    check if user wants calculation continue.\n
    :param typing:
    :return: boolean
    """
    if typing == "y":
        return True
    else:
        return False


def calculate(first_number, next_number, operation):
    if operation == "+":
        print()
        return first_number + next_number
    elif operation == "-":
        return first_number - next_number
    elif operation == "*":
        return first_number * next_number
    elif operation == "/":
        return first_number / next_number


print(art.logo)

# new_calculation = True

while True:
    continue_calculation = True
    first_number = float(input("What's the first number?: "))
    print("+ \n- \n* \n/ \n")

    while continue_calculation:
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))

        calculate_result = calculate(first_number, next_number, operation)

        print(f"{first_number} {operation} {next_number} = {calculate_result}")
        continue_calculation = check_the_continue_calculation(input(
            f"Type 'y' to continue calculating with {calculate_result}, or type 'n' to start a new calculation").lower())

        if continue_calculation:
            first_number = calculate_result
