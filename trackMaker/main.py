import mesh_data_generator as mdg
import numpy as np
import pybullet as p
import pybullet_data as pd

import vertex_data_generator as vdg


def main():
    print("\n~ Welcome ~\n")
<<<<<<< HEAD
    mdg.gen_straight_verticies()
=======

    start_pos = [1, 2]
    end_pos = [4, 5]

    center_line = vdg.generate_straight_track(start_pos, end_pos)

    print(center_line)
>>>>>>> 863f4dde3ebe42c5cf0d5da9a5d438594b058acd

if __name__ == "__main__":
    main()