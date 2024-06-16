def check_start_with(string, prefix):
    return string.startswith(prefix)
def check_end_with(string, suffix):
    return string.endswith(suffix)
input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
if check_start_with(input_string, prefix):
    print(f"The string '{input_string}' starts with '{prefix}'.")
else:
    print(f"The string '{input_string}' does not start with '{prefix}'.")

if check_end_with(input_string, suffix):
    print(f"The string '{input_string}' ends with '{suffix}'.")
else:
    print(f"The string '{input_string}' does not end with '{suffix}'.")
