def initialize_variables():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def input_operation():
    print("\nAvailable operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter the number of your chosen operation (1-4): ")
    return choice

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def display_result(result):
    print(f"\nResult: {result}")

def calculator():
    while True:
        # Initialize variables
        num1, num2 = initialize_variables()

        # Input operation
        operation = input_operation()

        # Perform calculation based on operation
        if operation == '1':
            result = add_numbers(num1, num2)
        elif operation == '2':
            result = subtract_numbers(num1, num2)
        elif operation == '3':
            result = multiply_numbers(num1, num2)
        elif operation == '4':
            result = divide_numbers(num1, num2)
        else:
            result = "Invalid operation selected"

        # Display result
        display_result(result)

        # Ask if the user wants to perform another calculation
        another = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
