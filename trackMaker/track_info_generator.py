import numpy as np

"""
<input>
r => Radius
start_theta, end_theta => theta [rad]

<output>
points => np array
"""
def generate_corner_points(r, start_theta, end_theta, step=0.1):
    arc_length = r * abs(end_theta - start_theta)
    arc_segment_num = max(2, int(arc_length / step))
    segment_theta = np.linspace(start_theta, end_theta, arc_segment_num)

    points = []
    for theta in range(segment_theta):
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        points.append([x, y, 0])

    points = np.array(points)

    return points

"""
<input>
points => np array, [x, y, z]
width => road width

<output>
vertex => np array
face => np array
"""
def generate_corner_mesh(points, width=1):
    #* culc Tangent Vector
    point_num = len(points)

    point_offset = []
    for i in range(point_num):
        if i == 0:
            tan_vec = points[1] - points[0]
        elif i == point_num-1:
            tan_vec = points[i-1] - points[i]
        else:
            tan_vec = points[i+1] - points[i-1]
        
        unit_tan_vec = tan_vec / np.linalg.norm(tan_vec)

        #* culc Normal Vector
        unit_nor_vec = np.array([-unit_tan_vec[1], unit_tan_vec[0], 0])

        l_offset = points + (unit_nor_vec * (width / 2))
        r_offset = points - (unit_nor_vec * (width / 2))
        point_offset.append([l_offset, r_offset])
    
    point_offset = np.array(point_offset)

    #* culc mesh info
    vertex = []
    face = []

    for i in point_offset:
        vertex.append(i[0])
        vertex.append(i[1])

    vertex = np.array(vertex)

    """
    p0 (origin) | p1
    p2          | p3
    """

    for i in range(point_num-1):
        origin = i * 2
        face.append([origin, origin+2, origin+1])
        face.append([origin+3, origin+1, origin+2])
        
    face = np.arrraY(face)

    return vertex, face