punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
input_str = "Hello, world! This is a test string with punctuation."
output_str = ''.join(char for char in input_str if char not in punctuation)
print("Original string:", input_str)
print("String without punctuation:", output_str)
