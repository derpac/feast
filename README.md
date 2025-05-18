# feast
finite element analysis solver tool - feast

found an awesome book in the library about fea solvers that inspired me to make a basic fea solver for solid mechanics

## How to use feast

feast is designed to be lightweight and simple to use. Its applications in FEA are limited however effective. Currently (18/05/2025) feast is desinged to accept a json file containing a FEA problem for either 1d or 2d problems.


**example json file for 2d problem**

```json

{
  "nodes": {
    "1": [0, 0],
    "2": [1, 0],
    "3": [0, 1],
    "4": [1, 1]
  },
  "elements": {
    "1": { "type": "bar2d", "nodes": [1, 2] },
    "2": { "type": "bar2d", "nodes": [2, 4] },
    "3": { "type": "bar2d", "nodes": [4, 3] },
    "4": { "type": "bar2d", "nodes": [3, 1] },
    "5": { "type": "bar2d", "nodes": [1, 4] } 
  },
  "material": {
    "E": 200000000000,
    "A": 0.01
  },
  "boundary_conditions": {
    "displacements": {
      "1": [0, 0],
      "3": [0, 0]
    },
    "forces": {
      "4": [1000, -1000]
    }
  }
}

```

The Backend will take calculate displacements in the structure and log to console but there is more to come...


**The current road map for feast:**
- Phase 1: 
  - Implement:
    - 2d beam elements with 3dof (x,y,rotation)
    - 2d frame elements with axial and bending
- Phase 2:
  - Implement:
    - 3 node (triangle) elements
    - 4 node (quadrilateral) elements
- Phase 3:
  - Develop an easy to use front end for problem visualisation and problem initialisation
  - Investigate the implementation of a meshing algorithm to allow for use with external models
- Phase 4:
  - Further expand the solver to tackle 3d problems, dynamic analyses and non-linear problems.

---
