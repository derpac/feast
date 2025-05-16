def input(file_path):
    # dummy parser (update this for .msh or CSV parsing)
    return {}, {}



def solve_fea(nodes, elements):
    # placeholder for solver logic
    return {
        "displacements": {node: [0.0, 0.0] for node in nodes},  # return nonsense results for now
        "stresses": {el: 0.0 for el in elements}
    }
