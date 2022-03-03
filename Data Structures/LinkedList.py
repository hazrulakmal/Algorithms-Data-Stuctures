#linked list
#head & tail pointers

class Node:
    def __init__(self, item, next_pos):
        self.item = item
        self.next_pos = next_pos
        
    def items(self):
        return self.item
 
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None and self.tail == None
    
    def add(self, v):
        
        if self.head == None and self.tail == None:
            node = Node(v, None)
            self.head = node
            self.tail = node
        else:
            temp = Node(v, self.head)
            self.head = temp
        
    def addatEnd(self, v):
        node = Node(v, None)
        
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
            
        else:
            self.tail.next_pos = node
            self.tail = node
            
    def get_front(self):
        return self.head
    
    def get_back(self):
        return self.tail
            
            