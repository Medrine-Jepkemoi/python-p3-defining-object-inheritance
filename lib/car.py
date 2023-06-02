from vehicle import Vehicle


class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

my_car = Car(4, 56)
print(my_car.go())
print(Car.__bases__)
