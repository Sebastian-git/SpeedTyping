data = open("words.txt", "r").read().replace("\n", "")

newData = ""
prev = ""
for char in data:
    if char == " " and prev != " ":
        newData += char
    elif char != " ":
        newData += char
    
    prev = char

print(newData)