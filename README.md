# Djikstra's Algorithm
This Python script implements Dijkstra's algorithm to find the shortest path between nodes in a weighted graph. The graph is represented as a dictionary where keys are nodes and values are lists of tuples (neighbor, weight).

# Functions
```python
dijkstra(graph, start, target=''): Calculates shortest paths from a starting node to all other nodes in a graph.
```
graph: A dictionary representing the graph.
start: The starting node for the algorithm.
target: An optional target node to print the path to.
Returns a tuple containing a dictionary of distances and a dictionary of paths.

# Usage
Create a graph as a dictionary of nodes and their neighboring nodes with weights.
Call the dijkstra function with the graph, starting node, and optional target node.
The function prints the shortest distance and path from the start node to the target node (or all nodes if no target is specified).

# Example
```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    # ... rest of the graph
}

dijkstra(my_graph, 'A', 'D')
```
