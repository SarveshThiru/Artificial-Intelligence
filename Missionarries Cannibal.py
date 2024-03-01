from collections import deque

def valid(state):
    M, C, boat = state
    if M < 0 or C < 0 or M > 3 or C > 3 or (C > M > 0):
        return False
    return True

def bfs():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    visited = set()
    queue = deque([([], initial_state)])

    while queue:
        path, current_state = queue.popleft()
        if current_state == goal_state:
            return path

        for dM, dC in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]:
            next_state = list(current_state)
            if current_state[2] == 1:  # boat is on the original side
                next_state[0] -= dM
                next_state[1] -= dC
                next_state[2] = 0
            else:  # boat is on the other side
                next_state[0] += dM
                next_state[1] += dC
                next_state[2] = 1
            next_state = tuple(next_state)

            if valid(next_state) and next_state not in visited:
                visited.add(next_state)
                next_path = path + [(dM, dC, current_state[2])]
                queue.append((next_path, next_state))

    return None

solution = bfs()
for step in solution:
    print(f"Move {step[0]} missionaries and {step[1]} cannibals to the {'other' if step[2] else 'original'} side.")
