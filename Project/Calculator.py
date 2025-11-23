############ CALCULATOR ###############

def addition(num_1, num_2):
    return num_1 + num_2


def subtraction(num_1, num_2):
    return num_1 - num_2


def multiplication(num_1, num_2):
    return num_1 * num_2


def division(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num_1 / num_2


def float_to_int(num):
    if num.is_integer():
        return int(num)
    return num



calc_dict = {'+': addition, '-': subtraction, '*': multiplication, '/': division}

print('CALCULATOR\n')

another_operation = True
while another_operation:
    print('Available Operations:')
    for key in calc_dict.keys():
        print(key)

    # Input 1st number (and validation)
    while True:
        try:
            num_1 = float(input("Enter the 1st number: "))
            num_1 = float_to_int(num_1)
            break
        except ValueError:
            print(f"Error: Please enter a valid 1st number")

    # Input 2nd number (and validation)
    while True:
        try:
            num_2 = float(input("Enter the 2nd number: "))
            num_2 = float_to_int(num_2)
            break
        except ValueError:
            print(f"Error: Please enter a valid 2nd number")

    while True:
            operation = input("\nChoose the operation (+, -, *, /): ")

            if operation not in calc_dict:
                print("Error: Invalid operation. Please choose from +, -, *, /.")
                continue

            try:
                result = calc_dict[operation](num_1, num_2)
                result = float_to_int(result)
                print(f"Result: {result}")
                break
            except ZeroDivisionError as e:
                print(f"Error: {e}")

    # Ask if the user wants to perform another operation
    while True:
        continue_calculation = input("\nDo you want to perform another operation? Enter 'yes' or 'no': ").lower()
        if continue_calculation in ['yes', 'no']:
            break
        else:
            print("Error: Please enter 'yes' or 'no'.")

    if continue_calculation == 'no':
        another_operation = False
        print("\nExiting calculator. Goodbye!")

