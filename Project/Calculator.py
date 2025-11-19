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


calc_dict = {'+': addition, '-': subtraction, '*': multiplication, '/': division}

print('CALCULATOR\n')

another_operation = True
num_1, num_2 = int, int

while another_operation:
    print('Available Operations:')
    for key in calc_dict.keys():
        print(key)

    check_for_1st_number = True
    check_for_2nd_number = True
    check_for_operation = True

    while check_for_1st_number:
        # Input validation for 1st number
        try:
            num_1 = float(input("Enter the first number: "))
            check_for_1st_number = False
        except ValueError:
            print(f"Error: Please enter valid first number")


    while check_for_2nd_number:
        # Input validation for 2nd number
        try:
            num_2 = float(input("Enter the Second number: "))
            check_for_2nd_number = False
        except ValueError as e:
            print(f"Error: Please enter valid second number")

    while check_for_operation:
        try:
            operation = input("\nChoose the operation (+, -, *, /): ")
            if operation not in calc_dict:
                raise ValueError("Invalid operation. Please choose from '+', '-', '*', or '/'.")
            check_for_operation = False

            result = calc_dict[operation](num_1, num_2)
            print(result)

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    input_validation = True
    # Ask if the user wants to perform another operation
    while input_validation:
        continue_calculation = input("\nDo you want to perform another operation? Enter 'yes' or 'no': ").lower()
        if continue_calculation in ['yes', 'no']:
            input_validation = False

            if continue_calculation == 'no':
                another_operation = False

