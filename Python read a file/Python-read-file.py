# Read a file
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

# Write a file
text = "Yooooooooo\nThis is some text\nHave a good one!\n"

with open('test.txt','w') as file:
    file.write(text)