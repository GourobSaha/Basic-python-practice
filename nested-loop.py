import time
# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter your symbol: ")

for i in range(rows):
    for j in range(columns):
        time.sleep(.3)
        print(symbol, end="")
    print()