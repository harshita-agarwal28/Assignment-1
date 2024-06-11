number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1
    for i in range(2, number + 1):
        result *= i
    print(f"The factorial of {number} is {result}.")
