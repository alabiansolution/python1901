print("Finding out the highest number")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

if num1 > num2 and num1 > num3:
    print(num1, "is the greatest of the numbers")
elif num2 > num1 and num2 > num3:
    print(num2, "is the greatest of the numbers")
else:
    print(num3, "is the greatest of the numbers")
