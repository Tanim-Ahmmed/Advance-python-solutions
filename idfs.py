# Depth-Limited Search (helper function for IDDFS)
def dls(graph, node, target, depth):
    if depth == 0 and node == target:
        return True                   # Found target at correct depth

    if depth > 0:                     # Recur only if depth remains
        for neighbor in graph[node]:
            if dls(graph, neighbor, target, depth - 1):  # Go one level deeper
                return True

    return False                      # Target not found at this path

# Iterative Deepening DFS
def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):             # Try all depths up to max
        if dls(graph, start, target, depth):        # Run DLS for each depth
            print(f"Found {target} at depth {depth}")
            return True                             # Return if found
    print(f"{target} not found within depth {max_depth}")
    return False                                    # Return False if not found


# Representing a graph using a dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],   # Node A connects to B and C
    'B': ['D', 'E'],   # Node B connects to D and E
    'C': ['F'],        # Node C connects to F
    'D': [],           # D has no neighbors
    'E': ['F'],        # E connects to F
    'F': []    
        }        # F has no neighbors
iddfs(graph, start='A', target='F', max_depth=3)
print("\n")