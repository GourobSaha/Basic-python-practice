# if statement = a block of code that will execute if it's condition is true
# logical operators (and,or,not) = used to check if two or more conditional statements is true

Age = int(input("Enter your age: "))

if Age >= 40 and Age <= 60:
    print("You are middle aged")
elif Age >= 18 and Age <= 39:
    print("You are an adult")
elif Age >= 5 and Age <= 17:
    print("You are a child")
elif Age < 1:
    print("You haven't born yet")
elif (Age >= 90 or Age <= 4):
    print("You need a diaper")
elif Age >= 61:
    print("You are old")
else:
    print("It's not a proper age")
