number=int(input("enter number:"))
total_sum = 0
while number > 0:
    digit = number % 10
    total_sum += digit
    number = number // 10
print(f"The sum of the digits of {number} is {total_sum}")
