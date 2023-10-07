class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_vertex):
        visited = set()

        def dfs_recursive(vertex):
            visited.add(vertex)
            print(vertex, end=' ')

            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start_vertex)

# Example usage:
if __name__ == "__main__":
    graph = Graph()

    # Add edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    start_vertex = 0
    print(f"Depth-First Traversal starting from vertex {start_vertex}:")
    graph.dfs(start_vertex)
