DOB= int (input (' please put in the date of the birth'))
month = int(input (' please put in the month' ))
year = int(input(' please put in the year'))
days=0
for i in (year, 2016):
    if i%4==0:
        days=days+366
    else:
        days= days + 365

print (days)


