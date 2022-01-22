
# Open file and read its content
file_content = open('37336.txt').read()

# Split text by newline, do not forget to remove empty string
num_list = file_content.split("\n")[:-1]
num_list = [int(num) for num in num_list]

counter = 0
max_pair = 0

for i in range(len(num_list)-1):
    if num_list[i] % 3 == 0 or num_list[i+1] % 3 == 0:
        counter += 1
        max_pair = max(max_pair, num_list[i] + num_list[i+1])

print(counter, max_pair)