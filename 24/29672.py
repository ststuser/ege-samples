# Open file and read its content
file_content = open('29672.txt').read()

# Split text by newline
string_list = file_content.split("\n")

# Do not forget to remove empty string. Now safe, avoiding situation when there is no empty string
try:
    string_list.remove("")
except ValueError:
    print("No empty string in file.")

# Variable to count defined strings
counter = 0

# Iterate through all strings in list
for string in string_list:
    # Check for the required condition to count
    if string.count("E") > string.count("A"):
        counter += 1

# Print required result
print(counter)
