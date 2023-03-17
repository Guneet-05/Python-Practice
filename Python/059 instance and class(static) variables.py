class Car:
    wheels = 4 #static or class variable
    def __init__(self) -> None:
        self.mileage = 10
        self.company = "BMW"

c1 = Car()
c2 = Car()

c2.mileage = 8

print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)

Car.mileage = 100 # this does not affect the objects
# because mileage is not a static variable

print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)
print(Car.mileage) # this will print 100

Car.wheels = 10
# This will affect every object because the wheels is a static data member

print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)

c1.wheels = 1000
print(c1.wheels) # this will be 1000
print(c2.wheels) # this will remain 10
print(Car.wheels) # this will also remain 10
