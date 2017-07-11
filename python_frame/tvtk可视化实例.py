from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop
 
plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",
        q_file_name="combq.bin",
        scalar_function_number=100, vector_function_number=200
    )#读入Plot3D数据
plot3d.update()#让plot3D计算其输出数据
grid = plot3d.output.get_block(0)#获取读入的数据集对象
 
con = tvtk.ContourFilter()#创建等值面对象  
con.set_input_data(grid)
con.generate_values(10, grid.point_data.scalars.range)#指定轮廓数和数据范围
 
#设定映射器的变量范围属性
m = tvtk.PolyDataMapper(scalar_range = grid.point_data.scalars.range,
                        input_connection=con.output_port)
a = tvtk.Actor(mapper = m)
a.property.opacity = 0.5#设定透明度为0.5
#窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()




from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop
 
#读入PLot3D数据
plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",
        q_file_name="combq.bin",
        scalar_function_number=100, vector_function_number=200
    )
plot3d.update()
grid = plot3d.output.get_block(0)
 
#对数据集中的数据进行随机选取，每50个点选择一个点
mask = tvtk.MaskPoints(random_mode=True, on_ratio=50)
mask.set_input_data(grid)
#创建表示箭头的PolyData数据集
glyph_source = tvtk.ConeSource()
#在Mask采样后的PolyData数据集每个点上放置一个箭头
#箭头的方向、长度和颜色由于点对应的矢量和标量数据决定
glyph = tvtk.Glyph3D(input_connection=mask.output_port,
                      scale_factor=2)
glyph.set_source_connection(glyph_source.output_port)
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=glyph.output_port)
a = tvtk.Actor(mapper=m)
 
#窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()



from tvtk.api import tvtk
from tvtk.common import configure_input
from tvtkfunc import ivtk_scene, event_loop
 
plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",
        q_file_name="combq.bin",
        scalar_function_number=100, vector_function_number=200
    )#读入Plot3D数据
plot3d.update()#让plot3D计算其输出数据
grid = plot3d.output.get_block(0)#获取读入的数据集对象
 
outline = tvtk.StructuredGridOutlineFilter()#计算表示外边框的PolyData对象
configure_input(outline, grid)#调用tvtk.common.configure_input()
m = tvtk.PolyDataMapper(input_connection=outline.output_port)
a = tvtk.Actor(mapper=m)
a.property.color = 0.3, 0.3, 0.3
 
#窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()