# Takes file and removes all new lines, quotes and apostrophes

# Specify which file to use for words.txt
file_name = "typingtest.py"
data = open(file_name, "r").read().replace("'", "").replace('"', "") # Removes new lines

newData = ""
prev = ""
for char in data:
    if char.isspace() and not (prev.isspace()): # Only allows one space at a time
        newData += " "
    elif not (char.isspace()):
        newData += char

    prev = char

# Writes new string to words.txt
txt = open("words.txt", "w")
txt.write(newData)
txt.close()