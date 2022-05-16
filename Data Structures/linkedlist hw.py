#Homework 6 
#Singly linked list

class Node:
    def __init__(self,item, next_item):
        self.item = item
        self.next = next_item

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        if self.isEmpty():
            temp = Node(item, self.head)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(item, self.head)
            self.head = temp
        
    def remove_front(self):
        newhead = self.head.next
        self.head = newhead
        
    def remove_end(self):
        remove_node = self.tail
        self.tail
