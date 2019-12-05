list1=['abc','pqr','xyz']
list2=[]
for i in range(len(list1)):
    second=list1[i]
    list1[i]=second[1:]

print (list1)

list3=[i for i[0][1:] in ['abc','xyz','pqr']]

print (list3)
