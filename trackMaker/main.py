import numpy as np
import pybullet as p
import pybullet_data as pd

import vertex_data_generator as vdg


def main():
    print("\n~ Welcome ~\n")

    vdg.generate_straight_track()

if __name__ == "__main__":
    main()