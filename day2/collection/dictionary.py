student = {
        "English":60,
        "Maths":70,
        "Biology" : 100,
        "Chemistry" : 50,
        "Physics" : 60
}

print(student["English"])

# Adding item in a list
student["CRK"] = 65
print(student)

# To remove item in a dictionary
student.pop("Chemistry")
print(student)
# To remove item in a dictionary
student.popitem()
print(student)

# using the del keywprd to delete items in a dictionary
del student["English"]
print(student)

student.clear()
print(student)

# dictionary constructor
states = dict("Imo"="Owerri", "Lagos"="Ikeja", "Akwa Ibom"="Uyo")
print(states)
