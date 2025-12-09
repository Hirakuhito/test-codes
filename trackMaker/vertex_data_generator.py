import numpy as np


def generate_straight_track(start_pos, end_pos, resolution=10):
    print("Generating straight track")

    """
    args:
        start_pos (list) : start position
        end_post (list) : end position
        width (float) : road width (default=2.0)
        resolution (int) : Number of road segments
    
    return:
        list : Generated coordinate's list [[x, y], [x, y], ...]
    """

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

    # --- 検算プロセス (2段階) ---
    # 検算1: 始点と終点が正しいか
    assert center_line[0] == start_pos, f"始点不一致: {center_line[0]} != {start_pos}"
    # 浮動小数点の誤差を考慮した終点チェック (abs(計算値 - 目標値) < 閾値)
    assert abs(center_line[-1][0] - x2) < 1e-9 and abs(center_line[-1][1] - y2) < 1e-9, \
           f"終点不一致: {center_line[-1]} != {end_pos}"
    
    # 検算2: 点の数が (分割数 + 1) になっているか
    assert len(center_line) == resolution + 1, f"点数不一致: {len(center_line)} != {resolution + 1}"
    
    return center_line