from collections import deque  # Import deque for efficient queue operations

def bfs(graph, start):
    visited = set()               # To keep track of visited nodes
    queue = deque([start])        # Initialize queue with the starting node

    while queue:                  # Run until the queue is empty
        node = queue.popleft()    # Remove and get the front node from the queue
        if node not in visited:   # Process the node if it's not visited
            print(node, end=' ')  # Print the node
            visited.add(node)     # Mark node as visited

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Representing a graph using a dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],   # Node A connects to B and C
    'B': ['D', 'E'],   # Node B connects to D and E
    'C': ['F'],        # Node C connects to F
    'D': [],           # D has no neighbors
    'E': ['F'],        # E connects to F
    'F': []    
        }        # F has no neighbors
bfs(graph, 'A')

print("\n")