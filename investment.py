class Investment:
    def __init__(self, principle, interest):
        self.principle = int(principle)
        self.interest = float(interest)

    def ROI(self, n):
        p = self.principle
        i = self.interest
        self.period = n 
        self.value  = (p * ((1 + i )**n))
        return self.value 
        
    def __str__(self):
        return 'principle is {} and interest is {}'.format(self.principle, self.interest)
i1= Investment(100, 0.10)

print (i1.principle, "is the principle", i1.interest, "is the interest", \
       "the return on investment is", i1.ROI(1))
print(i1)
