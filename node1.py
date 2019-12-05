''''
trying to understand node shit
'''




class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0

    def addVal(self, val):
        n = node(val)
        if self.head == None:
            self.size = n
            
        
