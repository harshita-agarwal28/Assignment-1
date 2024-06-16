numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = float('inf')
max_value = float('-inf')
for number in numbers:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number
print("The minimum value in the list is:", min_value)
print("The maximum value in the list is:", max_value)
