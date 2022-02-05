
# Open file and read its content
file_content = open('37336.txt').read()

# Split text by newline, do not forget to remove empty string
num_list = file_content.split("\n")[:-1]

# Change numbers type to integer to perform math operations
num_list = [int(num) for num in num_list]

# Variable to count defined pairs
counter = 0
# Variable to search for max pair sum; set to minimal possible sum.
max_pair = -20000

# Iterate through all possible indexes, except the last (to avoid IndexError)
for i in range(len(num_list)-1):
    # Check for the required pair condition
    if num_list[i] % 3 == 0 or num_list[i+1] % 3 == 0:
        # Increment counter
        counter += 1
        # Check and save maximum sum
        max_pair = max(max_pair, num_list[i] + num_list[i+1])

# Print required results
print(counter, max_pair)
