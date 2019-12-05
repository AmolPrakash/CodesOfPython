'''
computes the greatest common divisor

'''


#taking in input
x= int(input("please give 1st number : "))
y= int (input("please give 2nd number : "))
X=[]
Y=[]
#checking all divisible numbers
for i in range (1,x+1):
    if x%i==0:
        X.append(i)
for i in range (1, y+1):
    if y%i==0:
        Y.append(i)

#print (X,Y)
        
z=[]
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i]==Y[j]:
            z.append(X[i])
#print(z)
print("the greatest common divisor is ", z[-1])
#print(len(z))


