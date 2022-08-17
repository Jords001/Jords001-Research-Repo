##Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

dogAge = int(input("Enter Dogs Age: "))

if dogAge >2: #If the input dog age is larger than two create variables called firstTwo and olderThanTwo.
    firstTwo = 2 * 10.5 
    olderThanTwo = (dogAge -2) *4 #Take away the first two years then times by 4
    dogAgeHuman = firstTwo + olderThanTwo #Add the actual age of the first two years and the rest of the dogs age
else:
    dogAgeHuman = dogAge * 10.5 #Otherwise times the dog age by 10.5 because it is less than 2

print(dogAgeHuman)    
