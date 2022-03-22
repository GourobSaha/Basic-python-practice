
# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

# {} = format field
print("The {} jumped over the {}".format("cow","moon"))
print("The {0} jumped over the {1}".format(animal,item)) # positional arguments
print("The {1} jumped over the {0}".format(animal,item))
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))   # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow","moon"))

name = "Gourob"

print("My name is {}".format(name))
print("My name is {:10}".format(name,name))   # amount of padding
print("My name is {:<10}".format(name,name))  # < = left align
print("My name is {:>10}".format(name,name))  # > = right align
print("My name is {:^10}".format(name,name))  # ^ = center align


number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))