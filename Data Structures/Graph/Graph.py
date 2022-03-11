#Graph 
#All elements in the graphs are represented by nodes/vertices
#Relationships between each node are called edges
#The algorithm utilises linkedlist in particular Deque(python built-in linkedlist algorithm that generalises both stack and queue)

from collections import deque

class Node:
    
    def __init__(self, ids):
        self.id = ids
        # possibly other attributes
        # self.color = "red"
        self.color = "white"
        self.d = 0
        self.f = 0
        self.pi = None
        
class Graph:
    
    def __init__(self):
        self.n = 0
        self.V = []
        self.Adj = []
        self.time =0
        
    def __len__(self):
        return self.n
    
    def add_node(self):
        node = Node(self.n)
        self.n += 1
        self.V.append(node)
        self.Adj.append(deque())
        return node.id
    
    def get_node(self, ids):
        for v in self.V:
            if v.id == ids:
                return v
        return None
        
    def add_edges(self, u, v):
        # u and v must be an existed node
        self.Adj[u.id].append(v)
        self.Adj[v.id].append(u)
    
    def add_edge_using_ids(self, u_ids, v_ids):
        node_v = self.V[u_ids]
        node_u = self.V[v_ids]
        return self.add_edges(node_u, node_v)
    
    def add_directed_edge(self, u, v): 
        self.Adj[u.id].append(v)
		
	# add a directed edge using ids
    def add_directed_edge_using_ids(self, uid, vid):
        node_u = self.get_node(uid)
        node_v = self.get_node(vid)
        self.add_directed_edge(node_u,node_v)
    
    # display info about nodes	
    def display_nodes(self):
        print("id color d f pi:")
        for v in self.V: 
            if v.pi == None:
                print(v.color, v.d, v.f, "None") 
            else: 
                print(v.id, v.color, v.d, v.f, v.pi.id)
	
	# display graph itself		
    def display(self): 
        for i in range(0,self.n): 
            s = ""
            for v in self.Adj[i]: 
                vid = str(v.id)
                s = vid + " " + s 
            s = str(i) + ": " + s 
            print(s)








