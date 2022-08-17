isItAninteger = input("input a string: ")

def isFloat(num):
    try:
        float(num)
        return "is a float"
    except ValueError:
        return ""

if isItAninteger.isdigit(): ## .isdigit checks to see if it is a decimal number and then proceeds to print This string is an integer
    print("This string is an integer")
elif isFloat(isItAninteger):
    print("This string is a float")
else:
    print("This is not an integer")
