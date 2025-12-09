import numpy as np
import tqdm


def gen_straight_track(start_pos, end_pos, resolution=10, show=False):
    """
    args:
        start_pos (list) : start position
        end_post (list) : end position
        width (float) : road width (default=2.0)
        resolution (int) : Number of road segments
    
    return:
        list (np) : Generated coordinate's list [[x, y], [x, y], ...]
    """
    print("# Generating straight track data")

    if len(start_pos) != 2 or len(end_pos) != 2:
        raise ValueError("Position must be input [x, y] form.")
    
    if resolution < 1:
        raise ValueError("The number of divisions must be an integer greater than 1.")
    
    x1, y1 = start_pos
    x2, y2 = end_pos

    dx = (x2 - x1) / resolution
    dy = (y2 - y1) / resolution

    center_line = []
    for i in tqdm.tqdm(range(resolution + 1), desc='Coordinate'):
        x = round(x1 + dx * i, 3)
        y = round(y1 + dy * i, 3)
        center_line.append([x, y, 0])
    
    center_line = np.array(center_line)

    if show == True:
        print(f"# Straight track info : {type(center_line)}")
        print(f"{center_line}\n")

    return center_line

def gen_mesh_data(center_line, width=5.0, show=False):
    """
    args:
        center_line (list, np.array) : Generated center line points
        width (float) : Road width

    return:
        mesh_data (list, np.array) : This will be like [[v0, v2, v1], [v1, v3, v2], ...]
    """
    print("# Generating mesh data")

    n = len(center_line)
    left_offset = []
    right_offset = []

    #* Calcurate Vector
    for i in tqdm.tqdm(range(n), desc='Vector'):
        #* Tangent Vector
        if i == 0:
            tangent = center_line[1] - center_line[0]
        elif i == (n - 1):
            tangent = center_line[i] - center_line[i - 1]
        else:
            tangent = center_line[i + 1] - center_line[i - 1]
        
        unit_tan = tangent / np.linalg.norm(tangent)    #* Unit tangent Vector

        #*Normal Vector
        normal = np.array([-unit_tan[1], unit_tan[0], 0])
        left_offset.append(center_line[i] + normal * (width/2))
        right_offset.append(center_line[i] - normal * (width/2))

    left_offset = np.array(left_offset)
    right_offset = np.array(right_offset)

    #* Generate Vertices data
    vertices = []
    for L, R in tqdm.tqdm(zip(left_offset, right_offset)):
        vertices.append(list(L))
        vertices.append(list(R))
    
    vertices = np.array(vertices)

    faces = []
    for i in range(n-1):
        p0 = 2*i
        p1 = p0 + 1
        p2 = p1 + 1
        p3 = p2 + 1

        faces.append([p0, p2, p1])
        faces.append([p1, p3, p2])

    faces = np.array(faces)
    if show == True:
        print(f"# Verticies data : {type(vertices)}")
        print(f"{vertices}\n")

    return vertices, faces
