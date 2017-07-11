# -*- coding:utf-8 -*-
from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI
 
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
 
#创建一个带Crust（Python Shell）的窗口
gui = GUI()
win = ivtk.IVTKWithCrustAndBrowser()
win.open()
win.scene.add_actor(a)
 
#开始界面消息循环
gui.start_event_loop()


from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI
 
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
 
#创建一个带Crust（Python Shell）的窗口
gui = GUI()
win = ivtk.IVTKWithCrustAndBrowser()
win.open()
win.scene.add_actor(a)
     
#修正窗口错误
dialog = win.control.centralWidget().widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
dialog.show()
 
gui.start_event_loop()



from tvtk.api import tvtk
 
def ivtk_scene(actors):
    from tvtk.tools import ivtk
    #创建一个带Crust（Python Shell）的窗口
    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    win.scene.add_actor(actors)
    #修正窗口错误
    dialog = win.control.centralWidget().widget(0).widget(0)
    from pyface.qt import QtCore
    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show()
    return win
 
def event_loop():
    from pyface.api import GUI
    gui = GUI()
    gui.start_event_loop()
 
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()



def ivtk_scene(actors):
    from tvtk.tools import ivtk
    #创建一个带Crust（Python Shell）的窗口
    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    win.scene.add_actor(actors)
    #修正窗口错误
    dialog = win.control.centralWidget().widget(0).widget(0)
    from pyface.qt import QtCore
    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show()
    return win
 
def event_loop():
    from pyface.api import GUI
    gui = GUI()
    gui.start_event_loop()
    
    
    
    from tvtk.api import tvtk
from tvtkfunc import ivtk_scene,event_loop
 
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()




from tvtk.api import tvtk
import numpy as np
 
x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
r = tvtk.RectilinearGrid()
r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x),len(y),len(z)



from tvtk.api import tvtk
from tvtkfunc import ivtk_scene,event_loop
 
s = tvtk.STLReader(file_name = "python.stl")
m = tvtk.PolyDataMapper(input_connection = s.output_port)
a = tvtk.Actor(mapper = m)
 
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()


from tvtk.api import tvtk
 
def read_data():# 读入数据
    plot3d = tvtk.MultiBlockPLOT3DReader(
            xyz_file_name="combxyz.bin",#网格文件
            q_file_name="combq.bin",#空气动力学结果文件
            scalar_function_number=100,#设置标量数据数量
            vector_function_number=200#设置矢量数据数量
            )
    plot3d.update()
    return plot3d
 
plot3d = read_data()
grid = plot3d.output.get_block(0)