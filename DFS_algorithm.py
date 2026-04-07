def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reverse order to mimic recursive DFS
            stack.extend(reversed(graph.get(node, [])))

# Example adjacency list (graph)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Run DFS starting from node 1
print("DFS Traversal (Iterative):")
dfs_iterative(graph, 1)