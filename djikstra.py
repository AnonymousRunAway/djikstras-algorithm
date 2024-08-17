import heapq

def dijkstra(graph, start, target=''):
    """Calculates shortest paths from a starting node to all other nodes in a graph.

    Args:
        graph: A dictionary representing the graph, where keys are nodes and values are lists of tuples (neighbor, weight).
        start: The starting node for the algorithm.
        target: An optional target node to print the path to.

    Returns:
        A tuple containing a dictionary of distances and a dictionary of paths.
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f"\n{start}-{node} distance: {distances[node]}\nPath: {' -> '.join(paths[node])}")

    return distances, paths

def main():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        graph[node] = []

    num_edges = int(input("Enter the number of edges: "))

    for i in range(num_edges):
        node1, node2, weight = input(f"Enter edge {i+1} (node1 node2 weight): ").split()

        graph[node1].append((node2, int(weight)))
        graph[node2].append((node1, int(weight)))  # For undirected graph

    start_node = input("Enter the starting node: ")
    target_node = input("Enter the target node (optional, press Enter to skip): ")

    dijkstra(graph, start_node, target_node)

if __name__ == "__main__":
    main()
