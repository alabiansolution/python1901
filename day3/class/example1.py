class Fish:
    def __init__(self, name, skeleton, eyelid=True):
        self.name = name
        self.skeleton = skeleton
        self.eyelid = eyelid

    def details(self):
        print("The name of this fish is "+self.name+" and it is a "+self.skeleton+" fish"+" with an"+self.eyelid)


shark = Fish("Shark", "Catilagous", " eyelid")
shark.details()
