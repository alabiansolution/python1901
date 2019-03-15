num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

try:
    num3 = num1/num2
    print(num3)
except:
    print("Can not divide by zero")
