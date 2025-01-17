# Division of two numbers in Python

# Input from user
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Check if denominator is not zero
if num2 != 0:
    # Calculate the quotient
    quotient = num1 / num2
    # Display the result
    print(f"The result of dividing {num1} by {num2} is {quotient}")
else:
    # Handle division by zero
    print("Error: Division by zero is not allowed.")
