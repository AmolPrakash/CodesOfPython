'''Input= list(input("please give in a formula"))
opennum=0
clonum=0
pair=0

for i in range(len(Input)):
    if Input[i]=='(':
        opennum=+1
        for j in range(i,len(Input)):
            if Input[j]==')':
                clonum=+1
                pair+=1
            else:
                break
    else:
         print("please give bractes")
if pair%2==0 and (opennum)==(clonum):
    print("this can be formed")
else:
    print("this cannot be formed")





'''
#aditya sirs bracket cleaner

formula= input("enter")

stack=[]

balanced=True

for character in formula:
    if character=="(":
        stack.append(character)
    elif character==")":
        if len(stack)==0:
            balanced = False
        else:
            stack.pop(len(stack)-1)
            
if balanced and (len(stack) ==0) :
    print("good")
else:
    print("not good")
