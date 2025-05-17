from fea_1d import solve_fea_1d
from fea_2d import solve_fea_2d

def run_fea(data):
    element_type = next(iter(data['elements'].values()))['type']
    if element_type == "bar":
        return solve_fea_1d(data)
    elif element_type == "bar2d":
        return solve_fea_2d(data)
    else:
        raise ValueError("Unsupported element type: " + element_type)