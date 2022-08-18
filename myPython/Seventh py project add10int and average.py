list = []
numberOfInt = 10
for n in range(numberOfInt):
    numbers = int(input('Enter number: '))
    list.append(numbers)
average = sum(list) / len(list)
print(sum(list))
print(average)
