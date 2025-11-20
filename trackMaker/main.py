import numpy as np
import pybullet as p
import pybullet_data as pd



#* init engine
engine_id = p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())
p.setGravity(0, 0, -9.8)
p.resetSimulation()

#* make Ground 
ground_coll = p.createCollisionShape(p.GEOM_BOX, halfExtents=[50, 50, 0.1])
ground_vis = p.createVisualShape(
    p.GEOM_BOX,
    halfExtents=[50, 50, 0.1],
    rgbaColor=[0.6, 0.8, 0.6, 1]
) 

p.createMultiBody(
    baseMass=0,
    baseCollisionShapeIndex=ground_coll,
    baseVisualShapeIndex=ground_vis,
    basePosition=[0, 0, -0.1]
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
    rgbaColor=[0.3, 0.3, 0.3, 1]
)

#* road generate function
def create_straight(x, y, yaw, length=road_length):
    """generate straight road"""
    return p.createMultiBody(
        baseMass=0,
        baseCollisionShapeIndex=road_coll,
        baseVisualShapeIndex=road_vis,
        basePosition=[x, y, road_thicknes / 2],
        baseOrientation=p.getQuaternionFromEuler([0, 0, yaw])
    )

def create_curve(radius, start_angle, end_angle, arc_step=0.05):
    arc_length = radius * abs(end_angle - start_angle)
    num_points = max(2, int(arc_length / arc_step))

    angle_list = np.linspace(start_angle, end_angle, num_points)

    points = []
    #* calculate coordinate of each point
    for angle in range(angle_list):
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        points.append([x, y, 0])

    return np.array(points)



#* Automatic Course Generater
course_ids = []
for i in range(5):
    course_ids.append(create_straight(x= i * road_length * 0.9, y=0, yaw=0))

course_ids += create_curve(radius=5, angle=np.pi / 2, segments=20, start_angle=0)


#* Collision Detection to road (inside or outside)
"""
! I wonder make a program which do determine contact for each wheels.
"""
def is_on_road(car_id, road_ids):
    """Determine whether car is inside or outside on road."""
    for rid in road_ids:
        contacts = p.getContactPoints(car_id, rid)
        if len(contacts) > 0:
            return True
        
    return False



def main():
    print("\n<Welcome>\n")

    while True:
        p.stepSimulation()

        
if __name__ == "__main__":
    main()