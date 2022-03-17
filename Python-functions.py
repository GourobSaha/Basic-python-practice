#function = a block of code which is executed only when it is called.

def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age+1)+" years old")
    print("Have a nice day!")

hello("Gourob","Saha",21)
#hello("Mizan","Masum",22)


#return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)

print("Your lucky number is "+str(x))