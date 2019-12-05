userInput=str(input("Please give an input : "))
Output=[]
for i in range(len(userInput)-1,-1,-1):
    Output.append(userInput[i])
    

a= ''.join(Output)
print (a)


#alternate way


String_Output=''
for i in range(len(userInput)-1,-1,-1):
    String_Output=String_Output + userInput[i]

print(String_Output)
    
    
#using list index

print (userInput[::-1])

   
