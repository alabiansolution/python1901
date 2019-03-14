number = int(input("Enter number: "))

if number % 2 == 0:
    print(number, "is an even number")
if number % 2 == 1:
    print(number, "is an odd number")
if number > 1 and (number/number == number or number % 2 != 1):
    print(number, "is a prime number")
