# -*- coding:utf-8-*-
""""""
from mayavi import mlab
from os.path import join
import tarfile
 
#��ȡtarѹ���ļ�
dragon_tar_file = tarfile.open('dragon.tar.gz')
try:
    os.mkdir('dragon_data')
except:
    pass
dragon_tar_file.extractall('dragon_data')
dragon_tar_file.close()
dragon_ply_file = join('dragon_data', 'dragon_recon', 'dragon_vrip.ply')
 
# ��Ⱦdragon ply�ļ�
mlab.pipeline.surface(mlab.pipeline.open(dragon_ply_file))
mlab.show()
 
#ɾ����ѹ���ļ���
import shutil
shutil.rmtree('dragon_data')


import zipfile
import numpy as np
from mayavi import mlab
 
#��ȡѹ���ļ�
hgt = zipfile.ZipFile('N36W113.hgt.zip').read('N36W113.hgt')
data = np.fromstring(hgt,'>i2')
data.shape = (3601, 3601)
data = data.astype(np.float32)
data = data[:1000, 900:1900]
data[data == -32768] = data[data > 0].min()
 
#��Ⱦ����hgt������data
mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))
mlab.surf(data, colormap='gist_earth', warp_scale=0.2,
            vmin=1200, vmax=1610)
 
#����ڴ�
del data
#��������ʽ�Ŀ��ӻ�����
mlab.view(-5.9, 83, 570, [5.3, 20, 238])
mlab.show()



# ���о�γ������
cities_data = """
Bei Jing, 116.23,39.54
Shang Hai, 121.52, 30.91
Hong Kong,114.19,22.38
Delhi,77.21,28.67
Johannesburg,28.04,-26.19
Doha,51.53,25.29
Sao Paulo,-46.63,-23.53
Toronto,-79.38,43.65
New York,-73.94,40.67
San Francisco,-122.45,37.77
Dubai,55.33,25.27
Sydney,151.21,-33.87
"""
########## ��ȡ����#########
# ��������-���������ֵ䡢���о�γ�ȵ��б�
import csv
cities = dict()
coords = list()
for line in list(csv.reader(cities_data.split('\n')))[1:-1]:
    name, long_, lat = line
    cities[name] = len(coords)
    coords.append((float(long_), float(lat)))
 
########## ����ת��##########
# ����γ�ȵ�λ��ת��Ϊ��ά����
import numpy as np
coords = np.array(coords)
lat, long = coords.T * np.pi / 180
x = np.cos(long) * np.cos(lat)
y = np.cos(long) * np.sin(lat)
z = np.sin(long)
 
##########��������##########
from mayavi import mlab
mlab.figure(bgcolor=(0.48, 0.48, 0.48), size=(400, 400))
 
##########���Ƶ���##########
# ���ư�͸�������ʾ����
sphere = mlab.points3d(0, 0, 0, scale_factor=2,
                                color=(0.67, 0.77, 0.93),
                                resolution=50,
                                opacity=0.7,
                                name='Earth')
 
# �������淴�����
sphere.actor.property.specular = 0.45
sphere.actor.property.specular_power = 5
# ���ñ����޳����Ը��õ���ʾ͸��Ч��
sphere.actor.property.backface_culling = True
 
##########���Ƴ���##########
# ���Ƴ���λ��
points = mlab.points3d(x, y, z, scale_factor=0.03,color=(0, 0, 1))
# ���Ƴ�������
for city, index in cities.items():
    label = mlab.text(x[index], y[index], city,
                      z=z[index], color=(0,0,0),
                      width=0.016 * len(city), name=city)
     
##########���ƴ��ޱ߽�##########
from mayavi.sources.builtin_surface import BuiltinSurface
continents_src = BuiltinSurface(source='earth', name='Continents')
# ����LODΪ2
continents_src.data_source.on_ratio = 2
continents = mlab.pipeline.surface(continents_src, color=(0, 0, 0))
 
##########���Ƴ��##########
theta = np.linspace(0, 2 * np.pi, 100)#ƽ��360Ϊ100��
x = np.cos(theta)
y = np.sin(theta)
z = np.zeros_like(theta) 
mlab.plot3d(x, y, z, color=(1, 1, 1),opacity=0.2, tube_radius=None)
##########��ʾ�ɽ�������##########
mlab.view(100, 60, 4, [-0.05, 0, 0])
mlab.show()