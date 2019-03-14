class Car:
    battery = 1
    seat = 4
    name = "Toyota"
    model = "Camry 2010"
    color = "Red"

    def __init__(self, displacement, time):
        self.displacement = displacement
        self.time = time

    def details(self):
        print("Car name "+self.name+" Battery is "+str(self.battery)+" Model is "+self.model)

    def speed(self):
        speed = str(self.displacement / self.time) + "m/s"
        print(speed)

# Toyota = Car(3000, 2)
# Toyota.speed()
#
# opel = Car(2000, 5)
# opel.name = "Opel"
# opel.battery = 2
# opel.details()

class Convertible(Car):
     convertible = True
     def __init__(self, displacement, time):
         self.displacement = displacement
         self.time = time

toyota = Convertible(500, 3)
toyota.color = "Green"
print(toyota.speed())
print(toyota.color)
print(toyota.name)
print(toyota.model)
