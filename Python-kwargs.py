
# **kwargs =   parameter that will pack all arguments into a dictionary
#              useful so that a function can accept a varying amount of
#              keyword arguments

def hello (**names):
    print('Hello '+ names['first']+' '+ names['last']+'!')
    print('Hello',end=' ')
    for key,value in names.items():
        print(value, end=' ') # Will print all the values in the function

hello(title='Mr.',first='Gourob', middle='Saha', last='Surjo')