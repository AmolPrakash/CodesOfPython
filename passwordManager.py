class PasswordManager:
    def __init__ (self):
        #self.password = None
        self.oldPassword =[]
        
    def changePassword(self,a):
       # self.password = a
        if a in self.oldPassword:
            print ("error old password")
            return 
        self.oldPassword.append(a)
        
    def getPass(self):
        return(self.oldPassword[-1])
    
    def isCorrect(self, a):
        if self.oldPassword[-1] == a:
            return True
        else:
            return False

p = PasswordManager()
p.changePassword("123")
p.changePassword("abc")

p.changePassword("ABC")
p.changePassword("poop")
print (p.oldPassword)

print(p.isCorrect("poop"))
p.changePassword("123")
print(p.isCorrect("112"))
print(p.isCorrect("poop"))

        
    
    
    
