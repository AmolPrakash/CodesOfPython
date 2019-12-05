def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def numPal(n):
    temp = n
    rev = 0
    while n > 0:
        dig = n%10
        rev = rev*10 + dig
        n = n//10
    if temp == rev:
        return True
    else:
        return False

    
        
s = 'racecar'
a = 123321

print(palindrome(s))
print(numPal(a))



lyst = ['xyz','pqr','abc']

for i in range(len(lyst)):
    lyst[i] = lyst[i][1:]

print (lyst)


a = [[i,j] for i in range(2) for j in range(3)]
print(a)
import random
times = int(input(" num : "))
count = {k:None for k in range(2,13)}
for i in range(times):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sumDie = dice1 + dice2
    if count[sumDie] is None:
        count[sumDie] = 1
    else:
        count[sumDie] += 1

for i in range(2,13):
    percent = count[i]/times 
    print (i,"has the probablity to occour", percent *100, "%")

print (count)


import random

deck = [{'value': i, "suit" : c} for c in ['spades', 'clubs','hearts','diamonds']for i in range(2,15)]
random.shuffle(deck)
count = 0 

for i in range(100000):
    random.shuffle(deck)
    if  deck[0]['suit'] == deck[1]['suit'] == deck[2]['suit'] == deck[3]['suit'] == deck[4]['suit']:
        count += 1
    
print (count/10000)        
print (deck)
