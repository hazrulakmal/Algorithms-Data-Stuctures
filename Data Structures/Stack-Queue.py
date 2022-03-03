#Stack
#Last-in-First-Out
#works in single linked list with a head pointer

class Node:
    def __init__(self, item, next_pos):
        self.item = item
        self.next_pos = next_pos
        
    def items(self):
        return self.item

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, v):
        temp = Node(v, self.head)
        self.head = temp
        
    def pop(self):
        temp =  self.head
        self.head = temp.next_pos
        return temp.items()
        

#queue
#First-In-First-Out
#works in single linked list with head and tail pointer

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        
    def __len__(self):
        return self.len
    
    def enqueue(self, v):
        node = Node(v, self.head)
        
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
           
        else:
            self.tail.next_pos = node
            self.tail = node
        
        self.len += 1    
    
    def dequeue(self):
        
        temp = self.head
        self.head = temp.next_pos
        self.len -= 1
        return temp.items()














