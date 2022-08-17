##Month to Days

month = input('''Insert month shorthand eg Jan Feb Mar
: ''')

if month in ("Jan","jan","Mar", "mar","May","may","Jul","jul","Aug","aug","Oct","oct","Dec","dec"): 
    dayNum = 31
elif month in ("Apr","apr","Jun","jun","Sep","sep","Nov","nov",):
    dayNum = 30
else:
    dayNum = 28

print (dayNum)

## Initially didn't use in on line 6 and 8 and so the code didn't work as intended as it was looking for the whole array
