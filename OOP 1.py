'''
OOP 1
'''
# syntax : class className(parentClassName):
class Student(object):
    #state variables
        #syntax def __init__(parameters):
        #this is the constructor 
    def __init__(self, n, i, e,s=[]):
        # __init__ is the first one always
        #this is always referring to itself
        #over here you're creating  variable  
        self.name = n
        self._id = i
        self.email = e
        self.scores = s
# __init___ acts as a blue print which every element must follow


    def get_scores(self):
        return self.scores
    
    def add_scores(self, score):
        self.scores.append(score)

    def get_avg(self):
        sumAvg= 0
        for i in self.scores:
            sumAvg+=i
        return (sumAvg/ len(self.scores))
    
    def __str__(self):
        return "Name  : "+str(self.name)+ ",\n" + "ID : "+str(self._id) +\
            ",\n" +"Email : " + str (self.email) +" \n"

s1= Student("joe", 101, "joe@gmail.com")
##s1.get_scores()
##s1.add_scores(90)
##s1.add_scores(30)
##s1.add_scores(60)
s2 = Student("jim", 102, "jim@jimail.com", [30,90,60,60,70])

print(s1)

print(s2)
##print(s2.get_scores())
##print(s1.get_scores())
##print(s1.get_avg())
##print(s2.get_avg())
####        
