# *args =   parameter that will pack all arguments into a tuple
#                useful so that a function can accept a varying amount of arguments

def add(*Add):
    sum = 0
    Add = list(Add)
    Add[3] = 0  #fixing the value of fourth position by using list
    for i in Add:
        sum+=i
    return sum

print(add(1,2,3,4,5,6,7,8))