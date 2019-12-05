"""
string and a letter

"""

line=input("please give a sentence : ")
letter= input("letter pls : ")
j=0
found=False
while j < (len(line)):
    if letter==line[j]:
        print ("the index is", j)
        found=True
        break
    j+=1

if found==False:
    print("not found")
if letter not in line:
    print("letter not in sentence")
        

    
