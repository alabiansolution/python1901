student = ["Andrew", "Peter", "Philip", "Abosede"]
# Accessing items in a list
print(student[3])

# Changing items in a list
student[2] = "Benedict"
print(student[2])
print(student)

# Adding items in a list
student.append("Micheal")
print(student)

# Adding an item in any position
student.insert(1, "Godswill")
print(student)
# Remove item from a list
student.remove("Micheal")
print(student)
student.pop()
print(student)

# To determin the length of a list
print(len(student))

# Deleting item in a list
del student[0]
print(student)

# Deleting list
# del student
# print(student)

# Clearinge element in a list
student.clear()
print(student)

#list constructor
parents = list(("Mobolaji", "Adesanya", "Okoro", "Sanny", "Adesua"))
print(parents)
