def dls(graph, node, goal, depth, path):
    path.append(node)

    # Print every visited path
    print("Visited Path:", " → ".join(path))

    # If goal found
    if node == goal:
        return True

    if depth > 0:
        for neighbor in graph.get(node, []):
            if neighbor not in path:  # avoid cycles
                if dls(graph, neighbor, goal, depth - 1, path):
                    return True

    # Backtrack
    path.pop()
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n--- Depth Level {depth} ---")
        path = []
        if dls(graph, start, goal, depth, path):
            print("\n Goal Found!")
            print("Final Path:", " → ".join(path))
            return
    print("\n Goal not found within given depth")


# -- User Input --
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

# Run IDDFS
iddfs(graph, start, goal, max_depth)