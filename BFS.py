from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

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

    # Perform BFS starting from vertex 1
    print("BFS traversal starting from vertex 1:")
    g.bfs(1)
