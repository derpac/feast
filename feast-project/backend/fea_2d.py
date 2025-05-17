import numpy as np



def solve_fea_2d(data):
    nodes = data['nodes']
    elements = data['elements']
    material = data['material']
    bc_displacement = ['boundry_conditions']['displacements']
    bc_force = ['boundry_conditions']['forces']

    E = material['E']
    A = material['A']

    n_nodes = len(nodes)
    dof = 2 * n_nodes

    K = np.zeros((dof, dof))
    F = np.zeros(dof)

    for elem in elements.values():
        n1, n2 = elem['nodes']
        x1, y1 = nodes[str(n1)]
        x2, y2 = nodes[str(n2)]

        dx = x2 - x1
        dy = y2 - y1
        L = np.hypot(dx, dy)
        c = dx / L
        s = dy / L

        k = (E * A / L) * np.array([
            [ c*c,  c*s, -c*c, -c*s],
            [ c*s,  s*s, -c*s, -s*s],
            [-c*c, -c*s,  c*c,  c*s],
            [-c*s, -s*s,  c*s,  s*s]
        ])

        dofs = [2*(n1-1), 2*(n1-1)+1, 2*(n2-1), 2*(n2-1)+1]
        for i in range(4):
            for j in range(4):
                K[dofs[i], dofs[j]] += k[i, j]

    # apply force boundry conditions
    for nid, force in bc_force.items():
        idx = 2*(int(nid)-1)
        F[idx] = force[0]
        F[idx+1] = force[1]

    # apply displacement boundary conditions
    for nid, disp in bc_displacement.items():
        idx = 2*(int(nid)-1)
        for d in range(2):
            K[idx+d, :] = 0
            K[:, idx+d] = 0
            K[idx+d, idx+d] = 1
            F[idx+d] = disp[d]

    u = np.linalg.solve(K, F)
    return {
        str(i+1): [float(u[2*i]), float(u[2*i+1])]
        for i in range(n_nodes)
    }