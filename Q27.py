def string_to_list_method1(input_string):
    return list(input_string)
input_string = input("Enter a string: ")
char_list1 = string_to_list_method1(input_string)
print(f"List of characters from '{input_string}': {char_list1}")
