import numpy as np

"""
center_poins => [x, y, z]
"""
def gen_road_mesh(center_points, width=1.0):
    #* LR offset points
    left_offset_points = []
    right_offset_points = []
    
    #* number of center points
    N = len(center_points)

    for i in range(N):
        #* culc Tangent Vector
        if i == 0:
            tangent = center_points[i+1] - center_points[i]
        elif i == (N-1):
            tangent = center_points[i] - center_points[i-1]
        else :
            tangent = center_points[i+1] - center_points[i-1]

        #* Unit Vectorization
        unit_tan_vec = tangent / np.linalg.norm(tangent)

        #* culc Normal Vector
        normal = np.array([-unit_tan_vec[1], unit_tan_vec[0], 0])

        left_offset_points.append(center_points[i] + normal * (width / 2))
        right_offset_points.append(center_points[i] - normal * (width / 2))

    #* Array Update
    left_offset_points = np.array(left_offset_points)
    right_offset_points = np.array(right_offset_points)

    #* generate triangle mesh
    vertices = []
    faces = []

    for L, R in zip(left_offset_points, right_offset_points):
        """
        vertices => [L0, R0, L1, R1, L2, ...]
        """
        vertices.append(L)
        vertices.append(R)

    #* generate mesh point number
    for i in range(N-1):
        """
        L0=p0:0 | R0=p1:1
        L1=p2:2 | R1=p3:3
         ..  |  ..
        """

        p0 = 2 * i
        p1 = p0 + 1
        p2 = 2 * (i + 1)
        p3 = p2 + 1
    
        faces.append([p0, p1, p2])
        faces.append([p1, p2, p3])

    return np.array(vertices), np.array(faces)