class Node():
    def __init__(self, id, value, flag = None, edges = None):
        # int
        self._id = id
        # your object
        self.value = value
        #int
        self.flag = flag
        # set
        self.edges = edges
        
    def __eq__(self, node):
        return isinstance(node, Node) and self.id == node.id
    
    def __hash__(self):
        return hash(self.id)
    
    @property
    def id(self):
        return self._id
    
    def set_value(self, value):
        if not self.value:
            self.value = value
            return
        return
        
    def get_value(self):
        return self.value
    
    def set_edges(self, edges):
        for edge in edges:
            if not (edge in self.edges):
                self.add_edge(edge)
            
    def add_edge(self, edge):
        if not (edge in self.edges):
            self.edges.add(edge)
            
    def update_edge(self, node, weight):
        edge = Edge(node, weight)
        self.delete_edge(node)
        self.add_edge(edge)
        
    def delete_edge(self, node):
        edge = Edge(node)
        self.edges.discard(edge)
        
    def create_edge(self, node, weight = None):
        new_edge = Edge(node, weight)
        self.add_edge(new_edge)
        
    def is_neighbour(self, node):
        edge = Edge(node)
        if (edge in self.edges):
            return True
    def get_edges(self):
        return self.edges
        

class Edge():
    def __init__(self, node, weight = None):
        self.node = node
        self.weight = weight
    
    def __eq__(self, edge):
        return isinstance(edge, Edge) and self.node.id == edge.node.id
    
    def __hash__(self):
        return hash(self.node.id)
    
    @property    
    def tuple(self):
        tup = (self.node, self.weight)
        return tup
    
    @property
    def dict(self):
        dic = {'node': self.node, 'weight': self.weight}
        return dic
    
    def in_edge(self, node):
        
        if self.node == node:
            return (True, self.weight)

        return False

    def get_weight(self):
        return self.weight
    
class Graph():
    def __init__(self, weighted = False, directed = False, reflexive = False, symmetric = False, transitive = False):
        
        self.root = None
        
        # Graph characteristics
        self.weighted = weighted
        self.directed = directed
        
        # Relation characteristics
        self.reflexive = reflexive
        self.symmetric = symmetric
        self.transitive = transitive
        
    def set_relations(self, reflexive = False, symmetric = False, transitive = False):

        if  ((self.reflexive != reflexive) or 
            (self.symmetric != symmetric) or 
            (self.transitive != transitive)):
            
            self.reflexive = reflexive
            self.symmetric = symmetric
            self.transitive = transitive
            
            self.refactor()
            
        else:
            ...
            
    def refactor(self):
        ...
        
    def add_node(self):
        ...
        
    def remove_node(self):
        ...
        
    def is_connected(self):
        ...