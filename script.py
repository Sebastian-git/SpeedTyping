# Takes file and removes all new lines, quotes and apostrophes

data = open("typingtest.py", "r").read().replace("\n", "") # Removes new lines

newData = ""
prev = ""
for char in data:
    if char == "'" or char == '"': # Removes quotes and apostrophes
        pass
    else:
        if char == " " and prev != " ": # Only allows one space at a time
            newData += char
        elif char != " ":
            newData += char

    prev = char

# Writes new string to words.txt
txt = open("words.txt", "w")
txt.write(newData)
txt.close()