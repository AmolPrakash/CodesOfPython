import csv

csv.register_dialect('x',delimiter=',',skipinitialspace=False)

with open('/Users/amol/Library/Mobile Documents/com~apple~TextEdit/Documents/Untitled.csv','r') as a:
    data=csv.reader(a,dialect='x')
    for i in a:
        print (i)

