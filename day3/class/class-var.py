class Shark:
    location = "Ocean"
    animal_type = "Fish"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("The name is "+self.name+" with age of "+str(self.age)+" ",self.location)

    def swim_position(self):
        print(self.name+"swims forward")

sammy = Shark("Sammy", 40)
print(sammy.location)
print(sammy.animal_type)
sammy.details()

abosede = Shark("Abosede", 23)
abosede.location = "Nigeria"
print(abosede.location)
