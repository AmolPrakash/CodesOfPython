def get_mean(l):
    sum=0
    for x in l:
        sum += x
    return sum/len(l)

def get_std_dev(l):
    y=0
    for x in l:
        y+= (x-get_mean(l))**2
    return (y/len(l))**0.5

def divide_list(l,n):
    a=[]
    for x in l:
        a.append(x/n)
    return (a)


def multiply_list(l,a):
    l2=[x/a for x in l]
    return l2
    
    
        
def main():
    '''l1=[1,2,3,4,5,6]
    l2=[1,2,3]
    l3=[2,8]
    print (get_mean(l2))
    print(get_std_dev(l2))
    print(divide_list(l2,.5))
    print (multiply_list(l2,2))'''
    print("SAY MY NAME \n \n YOURE GODDAMN RIGHT")

if __name__=="__main__":
    main()
