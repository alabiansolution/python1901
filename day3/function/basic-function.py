
def greeting():
    print("Hello my people")

print(greeting())

def say_hello(name):
    print("Hello ", name)

say_hello("Benedict")
say_hello("Alabi")
say_hello("Dayo")

def person(name, age, color):
    print("My name is ", name, " I am",color," in complexion and I am ", age,"years old")

person("Benedict", 55, "Fair")
person("Alabi", 35, "Dark")

def add_numbers(num1, num2, num3):
    sum = num1 + num2 + num3
    print(sum)

add_numbers(2, 3, 4)

def grader(number):
    if number >= 70:
    	grade = "A"
    elif number >= 60 | number < 70:
    	grade = "B"
    elif number >= 50 | number < 60:
    	grade = "C"
    elif number >= 45 | number < 50:
    	grade = "D"
    elif number >= 40 | number < 45:
    	grade = "E";
    else:
    	grade = "F"
    print(grade)
grader(9)
