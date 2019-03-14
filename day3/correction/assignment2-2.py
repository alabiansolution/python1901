name = input("Enter name: ").capitalize()
# capitalize = name.capitalize()

presidents = ["Buhari", "Atiku", "Sowore", "Donal Duke", "Ezekwesili"]

for president in presidents:
    if president == name:
        print(name, "is contesting for President")
        break
    else:
        print(name, "is not contesting for President")
        break
