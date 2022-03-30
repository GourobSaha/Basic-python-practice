from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.model)
print(car_2.make)
print(car_1.year)
print(car_2.color)

car_1.wheels = 6

print(car_1.wheels)
print(car_2.wheels)

car_1.drive()
car_2.stop()