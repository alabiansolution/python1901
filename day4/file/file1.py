handle1 = open("demo.txt", "r")
print(handle1.read())

print("Reading certain part of a file")
handle2 = open("demo.txt", "r")
print(handle2.read(6))

print("Reading a line")
handle2 = open("demo.txt", "r")
print(handle2.readline())
