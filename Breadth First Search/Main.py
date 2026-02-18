from collections import deque

def bfs(graph, start_Node):
    visited = set()
    queue = deque([start_Node])
    visited.add(start_Node)

    print(f"Starting BFS traversal from the node: {start_Node}")
    while queue:
        current_Node = queue.popleft()
        print(current_ Node, end=" ")

        for Neighbor in graph[current_ Node]:
            if Neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

sample_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(sample_graph, 'A')
