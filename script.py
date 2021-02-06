# Takes file and removes all new lines, quotes and apostrophes

# Specify which file to use for words.txt
file_name = "words.txt"

# Saves entire file's contents into data
data = open(file_name, "r").read()

# Loop through each character, allow only one space, and continue to append it to the new data variable
newData = ""
prev = ""
for char in data:
    if char.isspace() and not (prev.isspace()): # Only allows one space at a time
        newData += " "
    elif not (char.isspace()):
        newData += char

    prev = char

# Writes new data to words.txt
txt = open("words.txt", "w")
txt.write(newData)
txt.close()