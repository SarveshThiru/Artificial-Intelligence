from constraint import Problem

def map_coloring_csp():
    problem = Problem()

    # Define variables (regions) and their possible values (colors)
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colors = ["Red", "Green", "Blue"]

    problem.addVariables(regions, colors)

    # Define constraints (no two adjacent regions can have the same color)
    problem.addConstraint(lambda wa, nt: wa != nt, ("WA", "NT"))
    problem.addConstraint(lambda wa, sa: wa != sa, ("WA", "SA"))
    problem.addConstraint(lambda nt, sa: nt != sa, ("NT", "SA"))
    problem.addConstraint(lambda nt, q: nt != q, ("NT", "Q"))
    problem.addConstraint(lambda sa, q: sa != q, ("SA", "Q"))
    problem.addConstraint(lambda sa, nsw: sa != nsw, ("SA", "NSW"))
    problem.addConstraint(lambda q, nsw: q != nsw, ("Q", "NSW"))
    problem.addConstraint(lambda q, v: q != v, ("Q", "V"))
    problem.addConstraint(lambda nsw, v: nsw != v, ("NSW", "V"))

    # Solve the CSP
    solutions = problem.getSolutions()

    return solutions

# Example usage:
if __name__ == "__main__":
    map_coloring_solutions = map_coloring_csp()

    if map_coloring_solutions:
        print("Map Coloring Solutions:")
        for solution in map_coloring_solutions:
            print(solution)
    else:
        print("No solutions found.")
