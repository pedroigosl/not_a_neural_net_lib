class Node():
    def __init__(self, id, value):
        
        self._id = id
        
        self.value = value
        
        self.edges = None
        
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
    
    @property    
    def value(self):
        return self.value
    
    @property
    def edges(self):
        return self.edges
        

class Edge():
    def __init__(self, node_a, node_b, weight = None):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight
        
    def as_tuple(self):
        return (self.node_a, self.node_b, self.weight)
    
    def as_dict(self):
        return {'node1': self.node_a, 'node2': self.node_b, 'weight': self.weight}
    
    def in_edge(self, node):
        result = (False, False)
        if self.node_a == node:
            result[0] = True
        if self.node_b == node:
            result[1] = True
        
        if result[0] or result[1]:
            return (True, result)
        return False

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