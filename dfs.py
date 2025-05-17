def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()             # Initialize the visited set on first call

    print(start, end=' ')           # Print the current node
    visited.add(start)              # Mark current node as visited

    # Recur for all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)





# Representing a graph using a dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],   # Node A connects to B and C
    'B': ['D', 'E'],   # Node B connects to D and E
    'C': ['F'],        # Node C connects to F
    'D': [],           # D has no neighbors
    'E': ['F'],        # E connects to F
    'F': []    
        }        # F has no neighbors
dfs(graph, 'A')

print("\n")