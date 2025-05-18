import numpy as np



def solve_fea_2d(data):
    nodes = data['nodes']
    elements = data['elements']
    material = data['material']
    bc_displacement = data['boundary_conditions']['displacements']
    bc_force = data['boundary_conditions']['forces']

    E = material['E']
    A = material['A']

    n_nodes = len(nodes)
    K = np.zeros((2 * n_nodes, 2 * n_nodes))
    F = np.zeros(2 * n_nodes)

    # Assemble global stiffness matrix
    for elem in elements.values():
        n1, n2 = elem['nodes']
        x1, y1 = nodes[str(n1)]
        x2, y2 = nodes[str(n2)]
        
        L = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        cx = (x2 - x1) / L
        cy = (y2 - y1) / L

        k_local = (E * A / L) * np.array([
            [ cx*cx,  cx*cy, -cx*cx, -cx*cy],
            [ cx*cy,  cy*cy, -cx*cy, -cy*cy],
            [-cx*cx, -cx*cy,  cx*cx,  cx*cy],
            [-cx*cy, -cy*cy,  cx*cy,  cy*cy]
        ])

        indices = [
            2 * (n1 - 1), 2 * (n1 - 1) + 1,
            2 * (n2 - 1), 2 * (n2 - 1) + 1
        ]

        for i in range(4):
            for j in range(4):
                K[indices[i], indices[j]] += k_local[i, j]

    # apply force boundary conditions
    for nid, force in bc_force.items():
        idx = 2 * (int(nid) - 1)
        F[idx] = force[0]
        F[idx + 1] = force[1]

    # apply displacement boundary conditions 
    for nid, disp in bc_displacement.items():
        idx = 2 * (int(nid) - 1)
        for d in range(2):  # x and y
            if disp[d] is not None:    #  fix for null y constrait issue
                dof = idx + d
                K[dof, :] = 0
                K[:, dof] = 0
                K[dof, dof] = 1
                F[dof] = disp[d]

    # solve
    u = np.linalg.solve(K, F)

    # return displacement 
    return {
        str(i + 1): [float(u[2 * i]), float(u[2 * i + 1])]
        for i in range(n_nodes)
    }