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
def gen_straight(x=0, y=0, length=5, width=1, step=0.1):
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

def gen_arc_points(r=1, start_theta=0, end_theta=np.pi/2, step=0.1):
    arc_length = r * abs(end_theta - start_theta)
    points_num = max(2, int(arc_length / step))
    theta_list = np.linspace(start_theta, end_theta, points_num)

    points = []
    for theta in theta_list:
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        points.append([x, y, 0])
    
    return np.array(points)


def gen_arc_mesh(points, width=1):
    """
    points => [x, y, 0]
    """

    offset_L = []
    offset_R = []

    N = len(points)

    #* culc vector
    for i in range(N):
        #* Tangent
        if i == 0:
            tan_vec = points[1] - points[0]
        elif i == (N-1):
            tan_vec = points[i] - points[i-1]
        else :
            tan_vec = points[i+1] - points[i-1]
        
        unit_tan_vec = tan_vec / np.linalg.norm(tan_vec)

        #* Normal
        normal = np.array([-unit_tan_vec[1], unit_tan_vec[0], 0])

        offset_L.append(points[i] + normal * (width / 2))
        offset_R.append(points[i] - normal * (width / 2))

    offset_L = np.array(offset_L)
    offset_R = np.array(offset_R)

    #* Generate triangle mesh
    vertices = []
    for L, R in zip(offset_L, offset_R):
        vertices.append(L)
        vertices.append(R)
    
    vertices = np.array(vertices)

    """
    p0 | p1
    p2 | p3
    """
    faces = []
    for i in range(N-1):
        p0 = i * 2
        p1 = p0 + 1
        p2 = p1 + 1
        p3 = p2 + 1

        faces.append([p0, p2, p1])
        faces.append([p3, p1, p2])
    
    faces = np.array(faces)

    return vertices, faces

#* save mesh point info as .obj
def save_as_obj(vertices, indices, filename):
    with open(filename, 'w') as f:
        #* write out vertices data
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        
        #* write out faces data
        for face in indices:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")

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

    gen_straight(length=2)

    points = gen_arc_points(step=0.1)
    vertices, faces = gen_arc_mesh(points)

    print(f"~ points : \n{points.tolist()}\n")
    print(f"~ vertices : \n{vertices.tolist()}\n")
    print(f"~ faces : \n{faces.tolist()}\n")

    save_as_obj(vertices, faces, "track_cata.obj")

    # arc_col = p.createCollisionShape(
    #     shapeType=p.GEOM_MESH,
    #     vertices=vertices,
    #     indices=faces
    # )

    while True:
        p.stepSimulation()


if __name__ == "__main__":
    main()