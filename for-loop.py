import time
# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#               while loop = unlimited
#               for loop = limited

for i in range(10):
    print(i+1)

for j in range(50,100,3):
    print(j+1)

for n in "Gourob Saha":
    time.sleep(1)
    print(n)

for s in range(10,0,-1):
    time.sleep(1)
    print(s)
print("Time's up!")