elements = [1, 2, 3, 2, 2, 4, 5, 2, 3, 4, 2]
target_element = 2
count = 0
for element in elements:
    if element == target_element:
        count += 1
print(f"The element {target_element} occurs {count} times in the list.")
