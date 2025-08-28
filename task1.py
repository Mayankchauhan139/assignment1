#Taking input for opration
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
# Performing operaations
print("\nAddition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)
print("Division:",num1/num2) if num2>0 else print("Division: Error! Division by zero is not allowed.")