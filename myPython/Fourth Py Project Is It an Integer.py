isItAninteger = input("input a string: ")

def isFloat(num): ## Define isFloat
    try:
        float(num) ##Try convert to float
        return "is a float"
    except ValueError:## Exception return nothing
        return ""

if isItAninteger.isdigit(): ## .isdigit checks to see if it is a decimal number and then proceeds to print This string is an integer
    print("This string is an integer")
elif isFloat(isItAninteger): ## As defined isFloat checks to see if the string is a float
    print("This string is a float")
else: ## Otherwise print this is not and integer
    print("This is not an integer")
