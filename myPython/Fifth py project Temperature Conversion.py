#******************************
#TEMPERATURE CONVERSION PROGRAM
#******************************
#Enter 1. For Celsius to Fahrenheit
#Enter 2. For Fahrenheit to Celsius
#Enter 3 to Quit: 2
#'''
print('''******************************
TEMPERATURE CONVERSION PROGRAM
******************************
Enter 1. For Celsius to Fahrenheit
Enter 2. For Fahrenheit to Celsius
Enter 3 to Quit:''')
check1 = True #loop that we can break out of in the if statement
option = int(input(""))
while (check1):
    if option == 1 or option == 2: #if option is 1 or 2 than break loop otherwise print and exit
        break
    else: print("option 1 or 2 not selected exiting...")
    exit()
temperature = int(input ("Temperature:"))

if option == 1:
    print((temperature * 9/5) + 32) # times temperature so that it is nine fifths or 1.8 it's value and then add 32
else:
    print((temperature - 32) * 5/9) # take away 32 from temperature then times by five nineths or 0.556
    
   
'''Initially I forgot to put double brackets so the print temperature was not calculating and was printing the same as the input
I also amongst trialing options bracketed unnecessarily eg (if option == (1))'''

##I made a second version of this script

check1 = True #loop that we can break out of in the if statement
option = (input(""))
while (check1):
    if option == "1" or option == "2": #if option is 1 or 2 than break loop otherwise print and exit
        break
    elif option == "3": ##else if option 3 exit and print exiting
        print("exiting")
        exit()
    else:
        print("unknown option please run again") ##else print unknown option and exit
        exit()
temperature = int(input ("Temperature:"))

if option == "1":
    print((temperature * 9/5) + 32) # times temperature so that it is nine fifths or 1.8 it's value and then add 32
    print("Farenheit") ##Print Farenheit the line under
else:
    print((temperature - 32) * 5/9) # take away 32 from temperature then times by five nineths or 0.556
    print("Celcius") ##Print Celcius the line under
