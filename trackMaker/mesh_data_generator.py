import numpy as np


def gen_straight_verticies(start_pos, end_pos, segments=10):
    print("# Generating straight_verticies")

    """
    args : 
        start_pos (list) : [x1, y1]   Etart position
        end_pos (list) : [x2, y2]     End position
        num_segments (int) : Number of divisions (default=10)

    return :
        list : Generated coordinate's list [[x, y], [x, y], ...]
    """

    if len(start_pos) != 2 or len(end_pos) != 2:
        raise ValuseError("Coordinate data is must be [x, y] form.")