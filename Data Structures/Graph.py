#Graph 
#All elements in the graphs are represented by nodes/vertices
#Relationships between each node are called edges
#The algorithm utilises linkedlist in particular Deque(python built-in linkedlist algorithm that generalises both stack and queue)

from collections import deque

class Node:
    
    def __init__(self, ids):
        self.id = ids
        
class Graph:
    
    def __init__(self):
        self.n = 0
        self.node_list = []
        self.adj_list = []
        
    def __len__(self):
        return self.n
    
    def add_node(self):
        node = Node(self.n)
        self.n += 1
        self.node_list.append(node)
        self.adj_list.append(deque())
        return node.id
    
    def get_node(self, ids):
        for v in self.node_list:
            if v.id == ids:
                return v
        return None
        
    def add_edges(self, u, v):
        # u and v must be an existed node
        self.adj_list[u.id].append(v)
        self.adj_list[v.id].append(u)
    
    def add_edges_byids(self, u_ids, v_ids):
        node_v = self.node_list[u_ids]
        node_u = self.node_list[v_ids]
        return self.add_edges(node_u, node_v)
    
x = Graph()

for i in range(6):
    x.add_node()
