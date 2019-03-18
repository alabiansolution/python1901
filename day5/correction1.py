firstname = input("Enter firstname: ")
middlename = input("Enter middlename: ")
lastname = input("Enter lastname: ")
fullname = firstname + middlename + lastname + "\n"

handle = open("demo1.txt", "a")
handle.write(fullname)
