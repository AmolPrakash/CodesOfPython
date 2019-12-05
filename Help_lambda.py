
def square (x):
    return x*x

sqr = lambda i: i*i

print(square(5))

print(sqr(5))


l1= [i for i in range(1,11)]
l2= list(filter(lambda i: (i%2==0),l1))
print(l1, l2)

l1= [i for i in range(1,10,2)]
l2= list(map(lambda i: (i**2),l1))
print(l1, l2)


l2= list(map(lambda i: (i**2),[i for i in range(1,10,2)]))
print(l2)

d=[{'name':'Todd','phone':'555-1414','email':'todd@mail.net'},
   {'name':'Helga','phone':'555-1618','email':'helga@mail.net'},
   {'name':'Princess','phone':'555-3141','email':''},
   {'name':'LJ','phone':'555-2718','email':'lj@mail.net'}]

for i in range(len(d)):
    if d[i]['phone'][-1]=="8":
        print("phone number ending with 8 \n", d[i],)
for i in range(len(d)):
    if  d[i]['email']=="":
        print("no emails: \n" , d[i])
