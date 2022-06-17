from typing import List, Any, Optional
from __future__ import annotations
import logging
import warnings
import time

log_date = str(time.strftime("%d-%m-%y_%H:%M:%S"))
log_name = f"logs/graph_{log_date}.log"
logging.basicConfig(filename=log_name, filemode='w', level=logging.DEBUG)
print(f"Session log started at {log_name}")

warnings.simplefilter("always")

warning = f" This library is a work in progress and not yet functional"
warnings.warn(warning, ResourceWarning)


class Node():
    def __init__(self, id, value, flag, edges):
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
        self.value = value
        
    def get_value(self):
        if not self.value:
            error = f" ValueError - No value declared in node #{self.id}"
            logging.error(error)
            raise ValueError()
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
    def __init__(self, root:Optional[Node] = None, weighted = False, 
                       directed = False, 
                       reflexive = False, 
                       symmetric = False, 
                       transitive = False):
        
        self.root = root
        self.nodes = set()
        self.last_id = 1
        
        # Graph characteristics
        self.weighted = weighted
        self.directed = directed
        
        # Relation characteristics
        self.reflexive = reflexive
        self.symmetric = symmetric
        self.transitive = transitive
        
    def set_relations(self, reflexive = False, symmetric = False, transitive = False):
        raise NotImplementedError
        if  ((self.reflexive != reflexive) or 
            (self.symmetric != symmetric) or 
            (self.transitive != transitive)):
            
            self.reflexive = reflexive
            self.symmetric = symmetric
            self.transitive = transitive
            
            info = (f" Relations' properties changed. New properties are:\n"
                    f" reflexive:     {reflexive}\n"
                    f" symmetric:     {symmetric}\n"
                    f" transitive:    {transitive}")             
            logging.info(info)
            self.refactor()
            
        else:
            info = (f" set_relations called, but no changes made. Current relations:"
                    f" reflexive:     {reflexive}\n"
                    f" symmetric:     {symmetric}\n"
                    f" transitive:    {transitive}")
            logging.info(info)
            warning = f" Relations already as defined"
            warnings.warn(warning, RuntimeWarning)
            ...
            
    def refactor(self):
        raise NotImplementedError
        ...
        
    def create_node(self, value: Any = None, flag: Any = None, edges: List[Edge] = None):
        raise NotImplementedError
        self.nodes.add(Node(self.last_id, value, flag, edges))
        self.last_id += 1
        ...
    
    def add_node(self, node: Node):
        warning = f" Using function with incomplete functionalities"
        warnings.warn(warning, ResourceWarning)
        
        if node.id < 0 or not isinstance(node.id, int):
            error = f" IndexError - id #{node.id} out of bounds"
            logging.error(error)
            raise IndexError
        elif node.id <= self.last_id:
            warning = f" ResourceWarning - node id #{node.id} not new"
            warnings.warn(warning, ResourceWarning)
            logging.warning(warning)
            if node in self.nodes:
                warning = f" ResourceWarning - node id #{node.id} in use, replacing node"
                warnings.warn(warning, ResourceWarning)
                logging.warning(warning)
                self.remove_node(node.id)
                
            self.nodes.add(node)
                
        self.last_id = node.id + 1
        info = f" Node with id #{node.id} added"
        logging.info(info)
        
        
    def remove_node(self, id):
        raise NotImplementedError
        ...
        
    def is_connected(self):
        raise NotImplementedError
        ...