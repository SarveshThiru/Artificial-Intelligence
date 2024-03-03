import heapq

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def calculate_manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = set()
    priority_queue = [Node(start, 0, calculate_manhattan_distance(start, goal))]
    
    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        current_position = current_node.position

        if current_position == goal:
            return current_node.cost

        if current_position in visited:
            continue

        visited.add(current_position)

        for direction in directions:
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

            if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols and grid[new_position[0]][new_position[1]] != 1:
                new_cost = current_node.cost + 1
                heuristic = calculate_manhattan_distance(new_position, goal)
                heapq.heappush(priority_queue, Node(new_position, new_cost, heuristic))

    return -1  # No path found

# Example usage:
if __name__ == "__main__":
    # Example grid (0 represents an open cell, 1 represents an obstacle)
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    shortest_path_cost = astar(grid, start, goal)

    if shortest_path_cost != -1:
        print(f"The shortest path cost from {start} to {goal} is: {shortest_path_cost}")
    else:
        print("No path found.")
