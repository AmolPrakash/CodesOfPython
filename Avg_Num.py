

def Average_Number(x):
    Sum=0
    for i in x:
        Sum+= i
    return (Sum/len(x))

def Standard_Deviation(x):
    y=Average_Number(x)
    l=[]
    for i in x:
        l.append(y-i)
        
    return l
        
def main():
    x=[1,2,3,4,5,6,7,8,9]
    print(Standard_Deviation(x))
    print (Average_Number(x))

if __name__== "__main__":
    main()


    
