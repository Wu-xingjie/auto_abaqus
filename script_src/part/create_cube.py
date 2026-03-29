from abaqus import *
from abaqusConstants import *
from caeModules import *
import regionToolset

# 在指定的模型中创建一个立方体
def create_cube(model, length, width, height):
    mdb = Mdb()
    if model not in mdb.models.keys():
        mdb.Model(model)
    target_model = mdb.models[model]

    # 创建草图
    s = target_model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    s.rectangle(point1=(-length/2, -width/2), point2=(length/2, width/2))

    # 拉伸生成立方体部件
    myPart = target_model.Part(name='Cube', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    myPart.BaseSolidExtrude(sketch=s, depth=height)

    # 删除临时草图
    del target_model.sketches['__profile__']