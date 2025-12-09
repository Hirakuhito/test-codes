import numpy as np
import pybullet as p
import pybullet_data as pd

import vertex_data_generator as vdg


def main():
    print("\n~ Welcome ~\n")

    start_pos = [1, 2]
    end_pos = [4, 5]

    center_line = vdg.generate_straight_track(start_pos, end_pos)

    print(center_line)

if __name__ == "__main__":
    main()