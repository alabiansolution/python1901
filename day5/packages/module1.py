
def user_input(name1, name2, name3):
    name4 = name1 + name2 + name3

    handle = open("demo2.txt", "a")
    handle.write(f"{name1} {name2} {name3} \n")
