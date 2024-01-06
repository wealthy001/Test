
# Calculator program

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbersdef subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Function to calculate the square root of a number
def square_root(num):
    return num ** 0.5

# Main function
def main():
    print("Calculator Program")
    print("-------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exit")

    while True:
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print("Result:", result)

        elif choice == 2:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice == 3:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice == 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            print("Result:", result)

        elif choice == 5:
            num = float(input("Enter the number: "))
            result = square_root(num)
            print("Result:", result)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
