t= int(input("please input time in 24hr format: "))
if t<12:
    print(t,"AM")
elif t==24:
    print ("00 AM")
else:
    t=t%12
    print(t,"PM")
    
