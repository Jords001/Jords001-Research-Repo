##Month to Days

month = input('''Insert month shorthand eg Jan Feb Mar
: ''')

if month in ("Jan","jan","Mar", "mar","May","may","Jul","jul","Aug","aug","Oct","oct","Dec","dec"): ##if input variable month is in array dayNum=31
    dayNum = 31
elif month in ("Apr","apr","Jun","jun","Sep","sep","Nov","nov",): ##if input variable month is in array dayNum=30
    dayNum = 30
else: ##Otherwise dayNum = 28
    dayNum = 28

print (dayNum) ##Print dayNum

## Initially didn't use in on line 6 and 8 and so the code didn't work as intended as it was looking for the whole array
