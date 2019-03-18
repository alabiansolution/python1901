from packages.module1 import user_input


firstname = input("Enter firstname: ")
middlename = input("Enter middlename: ")
lastname = input("Enter lastname: ")
enter_user = user_input(firstname, middlename, lastname)

print(enter_user)
