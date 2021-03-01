import numpy as np
import random 
import math 
import bpy



#distribution = stats.vonmises.pdf(np.linspace(-np.pi,np.pi,2000),Cp)*np.pi/1000
alpha = 0.05
angles = open(bpy.path.abspath("//Cp001.txt"),'r').read().split('\n')
fibre_diameter = 0.01
Cp = 0.001
w = 2
L = 0.2
length_fibres = 1
N = (4*alpha*L*w**2)/(length_fibres*np.pi*fibre_diameter**2)
print(N)

def create_cylinder(position = [0,0,0], rotation = [0,0,0], scale = [0.01,0.01,0.3]):
    
    bpy.ops.mesh.primitive_cylinder_add()
    so = bpy.context.active_object
   
    
    ## Define the position of the cylinder ##

    so.location[0] = position[0]
    so.location[1] = position[1]
    so.location[2] = position[2]

    ## Define the rotation of the cylinder ##
    so.rotation_euler[0] += rotation[0]
    so.rotation_euler[1] += rotation[1]
    so.rotation_euler[2] += rotation[2]


    ## Define the size of the cylinder ##
    so.scale[0] = scale[0]
    so.scale[1] = scale[1]
    so.scale[2] = scale[2]
    


for i in range(int(N)):
   create_cylinder(position = [float(np.random.rand()*L),
   random.choice((-1, 1))*float(np.random.rand()*w/2),
   random.choice((-1, 1))*float(np.random.rand()*w/2)], rotation = [float(angles[i]),0,0], 
   scale = [fibre_diameter/2,fibre_diameter/2,length_fibres/2])
   
   
#bpy.ops.mesh.primitive_cube_add()
#so = bpy.context.active_object
#so.scale[0] = L/2
#so.scale[1] = w/2
#so.scale[2] = w/2
#so.location[0] = L/2
#so.location[1] = 0
#so.location[2] = 0
