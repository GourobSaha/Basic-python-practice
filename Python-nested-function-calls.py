# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

num = input("Enter a number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)


# nested functions calls
print(round(abs(float(input("Enter a number: ")))))