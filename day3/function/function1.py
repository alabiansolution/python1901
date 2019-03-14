def person(name, age, title="Mr"):
    print("My name is ",title, name," I am ",str(age)+"years old.")

person("Benedict", 45)
person("Abosede", 22, "Mrs")


def times_table(number, start, stop):
    for increement in range(start, stop):
        print(number, " X ", increement, " = ", number*increement)


times_table(2, 2, 13)
times_table(3, 3, 10)
