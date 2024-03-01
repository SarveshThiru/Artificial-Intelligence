from collections import deque

def BFS(a, b, target):
    visited = {(0, 0): None}
    queue = deque([(0, 0)])

    while queue:
        state = queue.popleft()
        if state[0] == target or state[1] == target:
            return path(visited, state)
        for next_state in next_states(state, a, b):
            if next_state not in visited:
                visited[next_state] = state
                queue.append(next_state)

    return None

def next_states(state, a, b):
    x, y = state
    return [(a, y), (x, b), (0, y), (x, 0), (min(x + y, a), 0 if x + y <= a else y - (a - x)), (0 if x + y <= b else x - (b - y), min(x + y, b))]

def path(visited, state):
    if state is None:
        return []
    else:
        return path(visited, visited[state]) + [state]

a = 4  # capacity of jug A
b = 3  # capacity of jug B
target = 2  # target amount
print(BFS(a, b, target))
