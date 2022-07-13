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
        return self.head == None or self.tail == None
    
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
    
    def remove_end(self):
        if self.isEmpty() == False:
            head = self.head
            before = None
            while head != self.tail:
                before = head
                head = head.next_pos
            if before == None:
                self.tail = None
                self.head = None
            else:
                before.next_pos = None
                self.tail = before
            
    
    def remove_front(self):
        self.head = self.head.next_pos
    
class Queue:
    
    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None
        
    def __len__(self): #return the length of a queue
        return self.n
    
    def enqueue(self, new_item):
        if self.head == None and self.tail == None:
            node = Node(new_item, None)
            self.head = node
            self.tail = node
            self.n += 1
            
        else:
            node = Node(new_item, None)
            self.tail.next = node
            self.tail = node
            self.n += 1
            
    def deque(self):
        node = self.head
        self.head = self.head.next
        self.n -= 1
        return node.item
    
    def get_first(self):
        return self.head.item
            
            