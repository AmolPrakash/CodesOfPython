import csv
z=open('/Users/amol/Library/Mobile Documents/com~apple~TextEdit/Documents/Untitled.csv','r')
a=csv.reader(z)
for i in a:
    print (i)
z.close()
