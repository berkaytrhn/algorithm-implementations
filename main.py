from data_structures.non_linear.graph import Graph, NonLinearNode
from algorithms.sorting_algorithms.bfs import BFS
from typing import Any

graph = Graph(False)


graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(2,4)
graph.add_edge(4,5)
graph.add_edge(5,1)


graph.display()


bfs = BFS(graph, fields={"count": 0})
visited_nodes = []

def callback_method(fields: Any):
    print("Callback run!")
    fields["count"] += 1
    
print(graph.get_node(1).neighbours)
bfs.traverse(1, callback_method)

print(bfs.fields)