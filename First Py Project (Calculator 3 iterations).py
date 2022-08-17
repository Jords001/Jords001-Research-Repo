num1 = int(input("Enter First Number: ")) #Taking input of variable 1
opp = input ("Enter operator: ")
num2 = int(input("Enter Second Number: ")) #Taking input of variable 2
   
if (type(num1 or num2) != int):
        print("wrong input please enter a number")

if (opp == '+'):
        result = num1+num2
elif(opp == '-'):
        result = num1-num2
elif(opp == '/'):
        result = num1/num2
else:
        print("wrong input please enter an operator")    

print (result) #Print the sum of the two numbers
    
''' This was the initial idea behind the calculator project however this wouldn't work as the way python is programmed/written it would send an error because
as integer can't operate a string, it'd conclude this way before ever being able to execute the print wrong input line'''

check = True #The name of the loop
while(check): #While check is true run this loop
    try:
        num1 = int(input("Enter First Number: ")) #Taking input of variable 1
        opp = input ("Enter operator: ") # Taking input of operator
        num2 = int(input("Enter Second Number: ")) #Taking input of variable 2

        if (opp == '+'): # if operator equals + add variable 1 and 2
            result = num1+num2
        elif(opp == '-'): # if operator equals - minus variable 1 and 2
            result = num1-num2
        elif(opp == '/'): # if operator equals / divide variable 1 and 2
            result = num1/num2
        elif(opp == '*'): # if operator equals * times variable 1 and 2
            result = num1*num2
        else:
            print("wrong input please enter operator") # if the operator does not equal one of the above print this line

        print(result)    

    except:
       print("wrong input please try again") # if an exception (error) is made print this

       '''This worked well but it meant that if a mistake was made the whole process would have to start again
       I wanted to make it so that the loops were iterative, meaning you'd only have to try the step again'''
       
check1 = True #These are loops, each step has a loop so that if a mistake is made only the current loop has to be rerun rather than the whole code
check2 = True
check3 = True

masterCheck = True
while(masterCheck):
    while(check1):#This is the first loop and while check1 is true it will loop back unless reaching the break
        try: #This is the attempt eg try to run this code and if it fails/has an error run except.
            num1 = int(input("Enter First Number: ")) #Taking input of variable 1
        except:
            print("wrong input please try again") #This is the except, so if an error has occured it will run this code.
        else:
            break#The break here is exiting the loop

    while(check2):#Same as first loop but a second variation for a second number and step
        try:
            num2 = int(input("Enter Second Number: ")) #Taking input of variable 2
        except:
            print("wrong input please try again")
        else:
            break

    while(check3):
        try:
            opp = input ("Enter operator: ")#This is the operator input which will only accept + - * / and then does this to the numbers used for num1 and num2 otherwise it will print wrong input please enter operator

            if (opp == '+'): # if operator equals + add variable 1 and 2
                result = num1+num2
            elif(opp == '-'): # if operator equals - minus variable 1 and 2
                result = num1-num2    
            elif(opp == '*'): # if operator equals * times variable 1 and 2
                result = num1/num2
            elif(opp == '/'): # if operator equals / divide variable 1 and 2
                result = num1/num2
                
            else:
                print("wrong input please enter operator")
        except:
            print("wrong input please try again")

        else:
            break
        
    print(result)
    ch = input("Do you want to try again (Y/N): ")#This is a check input if answered yes Mastercheck which is the full loop will be set to false and the program will stop else it will loop again
    if (ch=='Y' or ch == 'y'):
        pass
    else:
        masterCheck = False
