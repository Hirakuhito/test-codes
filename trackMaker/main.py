import numpy as np
import pybullet as p
import pybullet_data as pd


#*=========== basic settings ==============
def init_engine():
    engine_id = p.connect(p.GUI)
    p.setAdditionalSearchPath(pd.getDataPath())
    p.setGravity(0, 0, -9.8)
    p.resetSimulation()

    return engine_id

#*=========== road generate =============
def gen_straight(x, y, length=5, width=1, step=0.1):
    col_id = p.createCollisionShape(
        shapeType=p.GEOM_BOX, 
        halfExtents=[length / 2, width / 2, 0.06]
    )
    vis_id = p.createVisualShape(
        shapeType=p.GEOM_BOX,
        halfExtents=[length / 2, width / 2, 0.06],
        rgbaColor=[0.3, 0.3, 0.3, 1],
        specularColor=[0, 0, 0]
    )
    road = p.createMultiBody(
        baseMass=0,
        baseCollisionShapeIndex=col_id,
        baseVisualShapeIndex=vis_id,
        basePosition=[x, y, 0]
    )

# def gen_curve():

# def gen_curve_points(r, start_theta, end_theta):
    


#*=========== main func ==============
def main():
    print("\n~~ WELCOME ~~\n")

    init_engine()

    #* generate field
    field_col_id = p.createCollisionShape(shapeType=p.GEOM_BOX, halfExtents=[25, 25, 0.05])
    field_vis_id = p.createVisualShape(
        shapeType=p.GEOM_BOX, 
        halfExtents=[25, 25, 0.05], 
        rgbaColor=[0.6, 0.8, 0.6, 1], 
        specularColor=[0, 0, 0]
    )
    field = p.createMultiBody(
        baseMass=0, 
        baseCollisionShapeIndex=field_col_id,
        baseVisualShapeIndex=field_vis_id,
        basePosition=[0, 0, 0] 
    )

    gen_straight()

    while True:
        p.stepSimulation(0, 0, 5)


if __name__ == "__main__":
    main()