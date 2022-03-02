# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        print(name)
        break

number = "191-15-2450"

for i in number:
    if i == "-":
        continue
    print(i, end="")
print("")


for j in range(1,16):
    if j == 13:
        pass
    else:
        print(j)