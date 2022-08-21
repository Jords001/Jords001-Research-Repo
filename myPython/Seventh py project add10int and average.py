list = []
numberOfInt = 10 ## Variable that contains the max for the numbers list range
for n in range(numberOfInt):
    numbers = int(input('Enter number: '))## This input will occur 10x
    list.append(numbers) ## appends an element to the end of the list can be str number object ect.
average = sum(list) / len(list) ## This variable adds the list together and then divides it by the amount of items in the list
print(sum(list))
print(average)
