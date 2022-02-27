# Type casting = convert a datatype of a value to another datatype
# User input = take value/s from user to perform certain operation

name = input("What is your name?: ")
age = input("What is your age?: ")
height = input("How tall are you?: ")

# We need to type cast age & height, otherwise these will remain string
age = int(age)+1
height = float(height)

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")


# Another way of type casting

name1 = input("What is your name?: ")
age1 = int(input("What is your age?: "))
height1 = float(input("How tall are you?: "))

age1 = age1+1

print("Hello "+name1)
print("You are "+str(age1)+" years old")
print("You are "+str(height1)+"cm tall")

