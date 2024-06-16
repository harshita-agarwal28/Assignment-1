source_file = 'source.txt'
destination_file = 'destination.txt'

try:
    with open(source_file, 'r') as f_source:
        content = f_source.read()
        with open(destination_file, 'w') as f_dest:
            f_dest.write(content)
    
    print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")

except FileNotFoundError:
    print("One of the files specified does not exist.")
except IOError as e:
    print(f"An error occurred: {e}")
