import pybullet as p
import pybullet_data as pd

#* init engine
engine_id = p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())
p.resetSimulationI()

#* make Ground 
ground_coll = p.createCollisionShape(p.GEOM_BOX, halfExtents=[50, 50, 0.1])
ground_vis = p.createVisionShape(
    p.GEOM_BOX,
    halfExtents=[50, 50, 0.1],
    rgbaColor=[0.6, 0.8, 0.6, 1]
) 

p.createMultiBody(
    baseMass=0,
    baseCollisionShapeIndex=ground_coll,
    baseVisionShapeIndex=ground_vis,
    basePosition=[0, 0, 0]
)

#* make Road
road_thicknes = 0.05
road_with = 2.0
road_length = 2.0

road_coll = p.createCollisionShape(
    p.GEOM_BOX,
    halfExtents=[road_length/2, road_with / 2, road_thicknes / 2]
)

road_vis = p.createVisualShape(
    p.GEOM_BOX,
    halfExtents=[road_length / 2, road_with / 2, road_thicknes / 2],
    rgbaColor=[0.1, 0.1, 0.1, 1]
)


def main():
    print("Welcome")





if __name__ == "__main__":
    main()