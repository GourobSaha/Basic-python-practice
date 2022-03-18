# keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesn't matter, unlike positional arguments
#                       Python knows the names of the arguments that a function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last+"!")


hello(last="Surjo",middle="Saha",first="Gourob")