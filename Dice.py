'''import random
num=0
result=[0,0,0,0,0,0,0,0,0,0]
while num<1000:
    a= random.randint(1,6) + random.randint(1,6)
    if a==2:
        result[0]=result[0] + 1
    elif a==3:
        result[1]=result[1] + 1
    elif a==4:
        result[2]=result[2] + 1
    elif a==5:
        result[3]=result[3] + 1
    elif a==6:
        result[4]=result[4] + 1
    elif a==7:
        result[5]=result[5] + 1
    elif a==8:
        result[6]=result[6] + 1
    elif a==9:
        result[6]=result[6] + 1
    elif a==10:
        result[7]=result[7] + 1
    elif a==11:
        result[8]=result
        [8] + 1
    else:
        result[9]=result[9] + 1
        
    num+=1

print (result)
    '''
result=[0 for i in range (13)]
import random
rolls= int(input("please give number of rolls"))

for i in range (rolls):
    dice1=random.randint(1,6)
    dice2= random.randint(1,6)
    idx=dice1+dice2
    result[idx]=result[idx]+1

print (result)

for i in range (2,13):
    print ("probability % of i: ", i , " is ", round((result[i]/rolls)*100),3) 
    

    
    
