str1='hello'
list1=[1,14,5,9,12]
list2=['one','two','three','four','five','six']
l3=[]
for i in range (len(list1)):
    if list1[i]<10:
        l3.append(list1[i])
print (l3)

l4=[]
for i in (list2):
    if len(i)==3:
        l4.append(i[0])
print (l4)
    
