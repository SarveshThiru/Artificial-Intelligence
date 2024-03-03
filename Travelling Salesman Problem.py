import itertools

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    all_permutations = itertools.permutations(cities)

    min_distance = float('inf')
    best_order = None

    for order in all_permutations:
        distance = calculate_total_distance(order, distances)
        if distance < min_distance:
            min_distance = distance
            best_order = order

    return best_order, min_distance

# Example usage:
if __name__ == "__main__":
    # Example distance matrix (replace with your own)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_order, min_distance = traveling_salesman_bruteforce(distance_matrix)

    print(f"Best order: {best_order}")
    print(f"Minimum distance: {min_distance}")
