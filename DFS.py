class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    # Perform DFS starting from vertex 1
    print("DFS traversal starting from vertex 1:")
    g.dfs(1)
