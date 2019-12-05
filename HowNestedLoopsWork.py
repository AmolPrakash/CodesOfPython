i=0
while True:
    print ("i=",i)
    i=i+1
    j=0
    while True:
        print("j=",j)
        j+=1
        z=0
        if j==3:
            print ("breaking inner loop")
            break
    if i==5:
        print ("breaking outer loop")
        break
