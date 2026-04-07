from sklearn import tree


def dfs_iterative(tree, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reverse order to maintain left-to-right traversal
            stack.extend(reversed(tree[node]))

print("\nDFS Traversal (Iterative):")
dfs_iterative(tree, 1)