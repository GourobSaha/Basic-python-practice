# variable = a container for a value. Behaves as the value that it contains.
# Datatype - String
First_name = "Gourob"
Last_name = "Saha"
Full_name = First_name+" "+Last_name
print(type(Full_name))
print("Hello "+Full_name)

# Datatype - int
age = 21
#age = age+1
age += 1
print(type(age))
print("You are "+str(age)+" years old now")

# Datatype - float
height = 175.56
print(type(height))
print("You are "+str(height)+" cm tall")

# Datatype - boolean
code = True
print(type(code))
print("I can do python: "+str(code))

# String Methods
name = "gourob"
print(len(name))
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*5)