from data_structures.non_linear import Graph
from data_structures.utils.node import NonLinearNode, LinearNode
from data_structures.linear.queue import Queue
from typing import Any, Callable, Optional


class BFS:
    
    def __init__(self, graph: Graph, fields: Optional[Any]=None) -> None:
        self.graph=graph
        self.queue: Queue=Queue()
        self.visited=set()
        self.fields=fields
    
    def traverse(self, value: Any, callback: Callable):
        """
        For this implementation, queue nodes are LinearNode,
        Graph nodes are NonLinearNode,
        Queue(Simple) implementation uses LinearNode with Any typed input value
        so, by calling enqueue with NonLinearNode it becomes like one 
        LinearNode of queue has a value which is a NonLinearNode:
        
        Queue:
        front -> LinearNode(
            value=NonLinearNode(value=Any, ...), 
            next=intermediate_node, 
            prev=None
        )
        intermediate_node -> LinearNode(
            value=NonLinearNode(value=Any, ...), 
            next=rear, 
            prev=None
        )
        rear -> LinearNode(
            value=NonLinearNode(value=Any, ...), 
            next=None, 
            prev=None
        )
    
        """
        start_node: NonLinearNode = self.graph.get_node(value)
        
        
        # print("start node")
        # print(start_node)
        self.queue: Queue=Queue()
        self.visited=set()
        self.queue.enqueue(start_node)

        
        # print(self.queue.rear)
        # print(self.queue.front)
        
        while not self.queue.isEmpty():
            current_node: LinearNode = self.queue.dequeue()
            
            
            
            if current_node.value not in self.visited:
                print(f"Visiting node: {current_node.value}")
                self.visited.add(current_node.value)
                
                
                # if there is a callback
                if callback:
                    callback(self.fields)
                
                # current_node: LinearNode
                # current_node.value:NonLinearNode
                # neighbour: NonLinearNode
                # print(f"Loop in neighbours for {current_node}")
                # print(current_node.value)
                for neighbour in current_node.value.neighbours:
                    #print(f"Neighbour: {neighbour}")
                    
                    if neighbour not in self.visited:
                        #print(f"neighbour not in visited: {neighbour}")
                        self.queue.enqueue(neighbour)
                    