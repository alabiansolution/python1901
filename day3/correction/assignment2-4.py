
numbers = [10, 20, 30, 40, 70, 200, 300]

numbers.append(200)
total = 0
for x in numbers:
    total += x
print("Total below")
print(total)

print("Average below")
average = total/len(numbers)
print(average)
