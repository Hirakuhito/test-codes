import pprint as pp

import numpy as np


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
    print("Generating straight track info")

    if len(start_pos) != 2 or len(end_pos) != 2:
        raise ValueError("Position must be input [x, y] form.")
    
    if resolution < 1:
        raise ValueError("The number of divisions must be an integer greater than 1.")
    
    x1, y1 = start_pos
    x2, y2 = end_pos

    dx = (x2 - x1) / resolution
    dy = (y2 - y1) / resolution

    center_line = []
    for i in range(resolution + 1):
        x = round(x1 + dx * i, 3)
        y = round(y1 + dy * i, 3)
        center_line.append([x, y])
    
    center_line = np.array(center_line)

    if show == True:
        print(type(center_line))
        print(center_line)

    return center_line

def gen_mesh_data(center_line, width=5):
    """
    args:
        center_line (list, np.array) : Generated center line points
        width (float) : Road width

    return:
        mesh_data (list, np.array) : This will be like [[v1, v3, v2], [v2, v4, v3], ...]
    """

    n = len(center_line)
    offset = []     #* [[left, right], [l, r], ...]

    #* Calcurate Tangent Vector
    for i in range(n):
        if n == 0:
            tangent = 0
    
    return "dammy data"
