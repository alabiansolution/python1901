
name = input("Enter name: ")
presidents = ["Buhari", "Atiku", "Sowore", "Jide Durosola", "Duke"]

for x in presidents:
    if name == x:
        print(name, "is contesting for president")
        break
    else:
        print(name.capitalize(), "is not contesting for president")
        break 
