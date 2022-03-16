# tuple =   collection which is ordered and unchangeable
#                used to group together related data

Identity = ("Gourob", 21, "male")

print(Identity.index("male"))
print(Identity.count(21))

for x in Identity:
    print(x)

if "Gourob" in Identity:
    print("Hello! Gourob")
else:
    print("Name not found!")
