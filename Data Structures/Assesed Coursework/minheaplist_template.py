class Node:
    def __init__(self,val,le,ri,pa):
        self.value = val
        self.left=le
        self.right=ri
        self.parent=pa

    # prints the whole tree below the current node
    def print(self):
        self.printrec(0)

    # recursively prints the values in the tree, indenting by depth
    def printrec(self,depth):
        print("    "*depth,end="") # right amount of indentation
        print(self.value)
        if self.left==None:
            print("    "*(depth+1),"None")
        else:
            self.left.printrec(depth+1)
        if self.right==None:
            print("    "*(depth+1),"None")
        else:
            self.right.printrec(depth+1)

class Item:
    def __init__(self,aroot,p,n):
        self.heap=aroot
        self.previous=p
        self.next=n

class MinHeaplist:
    def __init__(self):
        self.min = None
        self.head = None
        self.tail = None

    def insert(self,x):
        new_node = Node(x, None, None, None) #create single-element min-heap
        self.meld_into_rootlist(new_node) #add it to the rootlist
        if self.min == None:
            self.min = new_node
        else:
            if self.min.value > x:
                self.min = new_node
    
    def meld_into_rootlist(self, new_node):
        if self.head == None and self.tail == None:
            temp = Item(new_node, new_node, new_node)
            self.head = temp #keep track of rootlist elements
            self.tail = temp
        else:
            temp = Item(new_node, self.head, self.tail)
            current_node = self.tail
            current_node.previous = temp 
            self.head.next = temp
            self.head = temp
            
    
    def get_min(self):
        if self.min is None:
            return None
        return self.min.value
    
    def linkheaps(self,h1,h2):
    
    
    def iterate_node_child(self):
        se;f/
    
    def extractMin(self):
        z = self.min
        if z.left is not None and z.right is not None:
            #insert child nodes into rootlist
            children = [z.left, z.right]
            for i in range(0, len(children)):
                self.meld_into_rootlist(children[i])
                children[i].parent = None 
            self.remove_from_rootlist(z)
        return z
    
    def remove_from_rootlist(self, node):
        


    def print(self):
        h=self.min
        if h != None:
            print("-----")
            h.heap.print()
            h = h.next
            while h != self.min:
                print("-----")
                h.heap.print()
                h = h.next
            print("-----")



#if __name__ == '__main__':

#    H = MinHeaplist()

#   print("Inserting 5")
#    H.insert(5)
#    print("Inserting 3")
#    H.insert(3)
#    print("Inserting 7")
#    H.insert(7)
#    print("Inserting 6")
#    H.insert(6)
    #H.print()

    #print("Extracting ",H.extractMin())

#    print("The current min-heaplist:")
#    H.print()

#   print("Inserting 4")
#    H.insert(4)

#    print("The current min-heaplist:")
#    H.print()

#    n=H.min.next.heap.left
#    print("Decreasing key",n.value,"to 2")
#    H.decreaseKey(n,2)
#    H.print()



# The output produced:
# Inserting 5
# Inserting 3
# Inserting 7
# Inserting 6
# -----
# 3
#      None
#      None
# -----
# 6
#      None
#      None
# -----
# 7
#      None
#      None
# -----
# 5
#      None
#      None
# -----
# Extracting  3
# The current min-heaplist:
# -----
# 5
#     6
#         7
#              None
#              None
#          None
#      None
# -----
# Inserting 4
# The current min-heaplist:
# -----
# 4
#      None
#      None
# -----
# 5
#     6
#         7
#              None
#              None
#          None
#      None
# -----
# Decreasing key 6  2
# -----
# 2
#     7
#          None
#          None
#      None
# -----
# 5
#      None
#      None
# -----
# 4
#      None
#      None
# -----
# 
