# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "gourob Saha"

if(name[0].islower()):
    name = name.capitalize()
    print(name)


first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)