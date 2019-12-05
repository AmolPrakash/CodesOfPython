userInput = input("please give input : ")
cipher = ""
distance=int(input("please give distance : "))
userInput=userInput.upper()
for char in userInput:
    #cipher=cipher +  str((ord(char)+distance)
    ordVal=ord(char)
    cipherVal= ordVal + distance
    if cipherVal> ord('Z'):
        ciperVal = ord("A") + distance - (ord("Z") - ordVal +1)
    cipher+=chr(cipherVal)
print(cipher)

'''
for char in userInput:
    print(ord(char), end="")
'''

decipher=''

for i in range(0,len(cipher)-1,2):
    decipher = decipher + chr(int(cipher[i:i+2]))
print (decipher)
'''

decipher = ""

for i in range(0,len(cipher)-1,2):
    number= int(cipher[i] +cipher[i+1])
    decipher= decipher +chr(number)

print(decipher)
    '''

    
    
