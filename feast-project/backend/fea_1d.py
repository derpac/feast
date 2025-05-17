import numpy as np



def solve_fea_1d(data):
    nodes = data['nodes']
    elements = data['elements']
    material = data['material']
    bc_displacement = ['boundry_conditions']['displacements']
    bc_force = ['boundry_conditions']['forces']

    E = material['E']
    A = material['A']

    n_nodes = len(nodes)
    K = np.zeros((n_nodes, n_nodes))  
    F = np.zeros(n_nodes)

    # generate stiffness matrix 
    for elements in elements.values():
        n1,n2 = elements['nodes']
        x1,x2 = nodes[str(n1)][0], nodes[str(n2)][0]
        L = abs(x2 - x1) # define element length
        k_local = (E * A / L) * np.array([[1,-1], [-1,1]])

        i, j = n1 - 1, n2 - 1

        K[i, i] += k_local[0, 0]
        K[i, j] += k_local[0, 1]
        K[j, i] += k_local[1, 0]
        K[j, j] += k_local[1, 1]


    # apply force boundry conditions
    for node_id, value in bc_force.items():
        F[int(node_id) - 1] = value[0]    # x-direction in index 0 and y in index 1...

    # apply displacement boundry conditions
    for node_id, value in bc_displacement.items():
        idx = int(node_id) - 1
        K[idx, :] = 0
        K[:, idx] = 0
        K[idx, idx] = 1
        F[idx] = value[0]

    u = np.linalg.solve(K, F)
    
    return {str(i + 1): float(u[i]) for i in range(len(u))}
