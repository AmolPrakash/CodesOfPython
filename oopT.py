class Shape:
    def __init__(self):
        self.colour = (0,0,0)

class Rectangle(Shape):
    def __init__(self, a,b):
        Shape.__init__(self)
        self.length = a
        self.height = b
    def area(self):
        self.area = self.length * self.height
        return self.area
            
class Square(Rectangle):
    def __init__(self,a):
            Rectangle.__init__(self,a,a)
        self.length = a
    def area(self):
        self.area = self.length ** 2
        return self.area
            

    
        
    

s1 = Square(10)
print(s1.area,s1.length,s1.height, s1.colour)

