# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created

name = 'Saha' # global scope (available inside & outside functions)

def first_name():
    name = 'Gourob' # local scope (available only inside this function)
    print(name)

first_name()
print(name)