# -*- coding:utf-8 -*-
import numpy
from mayavi import mlab
 
x, y, z = numpy.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
scalars = x * x + y * y + z * z
obj = mlab.contour3d(scalars, contours=8, transparent=True)
mlab.show()


import numpy as np
from mayavi import mlab
 
def f(x, y):
    return np.sin(x - y)+np.cos(x + y)
 
x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
con_s = mlab.contour_surf(x, y, f)
mlab.show()


import numpy
from mayavi import mlab
 
s = numpy.random.random((10, 10))
img = mlab.imshow(s, colormap='gist_earth')
mlab.show()


import numpy as np
from mayavi import mlab
 
#建立数据
n_mer, n_long = 6, 11
dphi = np.pi / 1000.0
phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
mu = phi * n_mer
x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
z = np.sin(n_long * mu / n_mer) * 0.5
 
#对数据进行可视化
l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
mlab.show()




import numpy as np
from mayavi import mlab
 
#建立数据
t = np.linspace(0, 4 * np.pi, 20)
x = np.sin(2 * t)
y = np.cos(t)
z = np.cos(2 * t)
s = 2 + np.sin(t)
 
#对数据进行可视化
points = mlab.points3d(x, y, z, s, colormap="Reds", scale_factor=.25)
mlab.show()


import numpy as np
from mayavi import mlab
 
x, y, z = np.mgrid[-2:3, -2:3, -2:3]
r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
u = y * np.sin(r)/(r + 0.001)
v = -x * np.sin(r)/(r+0.001)
w = np.zeros_like(z)
 
obj = mlab.quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
mlab.show()




import numpy as np
from mayavi import mlab
 
def f(x, y):
    return np.sin(x - y)+np.cos(x + y)
 
x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
s = mlab.surf(x, y, f)
mlab.show()



import numpy as np
from mayavi import mlab
#建立数据
x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)
# 对数据进行可视化
mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')
# 更新视图并显示出来
mlab.show()





import numpy as np
from mayavi import mlab
 
######场景初始化######
figure = mlab.gcf()
# 用mlab.points3d建立红色和白色小球的集合
x1, y1, z1 = np.random.random((3, 10))
red_glyphs = mlab.points3d(x1, y1, z1, color=(1, 0, 0),
                           resolution=10)
x2, y2, z2 = np.random.random((3, 10))
white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9, 0.9, 0.9),
                             resolution=10)



# 绘制选取框，并放在第一个小球上
outline = mlab.outline(line_width=3)

outline.outline_mode = 'cornered'
outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
                  y1[0] - 0.1, y1[0] + 0.1,
                  z1[0] - 0.1, z1[0] + 0.1)
 
######处理选取事件#####
# 获取构成一个红色小球的顶点列表
glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()
#当选取事件发生时调用此函数
def picker_callback(picker):
    if picker.actor in red_glyphs.actor.actors:
        # 计算哪个小球被选取
        point_id = int(picker.point_id / glyph_points.shape[0])  # int向下取整        
        if point_id != -1:#如果没有小球被选取，则point_id = -1
            # 找到与此红色小球相关的坐标
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # 将外框移到小球上
            outline.bounds = (x - 0.1, x + 0.1,
                              y - 0.1, y + 0.1,
                              z - 0.1, z + 0.1)
 
picker = figure.on_mouse_pick(picker_callback)
mlab.title('Click on red balls')
mlab.show()


import numpy as np
x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)
 
from mayavi import mlab
from mayavi.tools import pipeline
src = mlab.pipeline.scalar_field(s)
mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.1)
mlab.pipeline.iso_surface(src, contours=[s.max()-0.1*s.ptp(), ])
mlab.pipeline.image_plane_widget(src,
                            plane_orientation='z_axes',
                            slice_index=10,
                        )
mlab.show()




import numpy as np
x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u =    np.sin(np.pi*x) * np.cos(np.pi*z)
v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)
 
from mayavi import mlab
mlab.quiver3d(u,v,w)
mlab.outline()
 
mlab.show()