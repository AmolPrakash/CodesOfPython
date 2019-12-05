class account(object):

    def __init__(self, name, account, balance = 0 ):
        self.name = name
        self.account = account
        self.balance = balance

    def getName(self):
        return self.name
    
    def changeName(self, name):
        self.name = name

    def getAccount(self):
        return self.account

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return (" Insufficient funds ")
        else:
            withdraw = self.balance - amount
            getBalance =- amount 
            return (" money withdrew : ", withdraw, "funds left : ",getBalance)
        
    def deposit(self, amount):
        getBalance+= amount
        

    def __str___(self):
        return "name : " + str(self.name) + "\n" + "account : " + str(self.account) + "\n" +\
               "balance : " +str(self.balance)

a1 = account("amol", 1, 1000)

print (a1)
        
