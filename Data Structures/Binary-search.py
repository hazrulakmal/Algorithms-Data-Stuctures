# Binary Decision Tree
# Name : Hazrul Akmal Hazarudin
# Group : 2
   
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def find_min(self):
        x = self.root
        while x.left != None:
            x = x.left
        return x.value
    
    def find_max(self):
        x = self.root
        while x.right != None:
            x = x.right 
        return x.value 
    
    def insert(self, x):
        if self.root is None:
            self.root = x
        else:
            y = self.root
            insert_recursive(None, y, x)
            
    def find(self, x):
        if self.root == None and self.root.value == x:
            return self.root


def insert_recursive(z, y, x):
    if y == None:
        if y.value >= x.value:
            y.left = x
        else:
            y.right = x
    else: 
        if x.val >= y.val:
            insert_recursive(y , y.right, x)
        else:
            insert_recursive(y, y.left, x)    
            