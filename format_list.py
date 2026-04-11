# Read lines from a file and convert them into a string + custom formatting

list1 = []

FILENAME = "text_to_list.log"
file_mode = 'r'

with open(FILENAME, file_mode) as text_file:
    for line in text_file:
        list1.append(line.rstrip())

for index in range(0, len(list1), 2):
    print("- " + list1[index] + " - " + list1[index + 1])
