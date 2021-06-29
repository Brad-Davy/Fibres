import numpy as np
import random 
import math 
import bpy
import time
import scipy


## Define parameters and ope  all text files ##
domain_cross_section = 400
my_scale = 1000
angles = open(bpy.path.abspath("//Cp001.txt"),'r').read().split('\n')
x_1 = open(bpy.path.abspath("//x_1.txt"),'r').read().split('\n')
x_3 = open(bpy.path.abspath("//x_3.txt"),'r').read().split('\n')
y_1 = open(bpy.path.abspath("//y_1.txt"),'r').read().split('\n')
y_3 = open(bpy.path.abspath("//y_3.txt"),'r').read().split('\n')
y_2 = open(bpy.path.abspath("//y_2.txt"),'r').read().split('\n')
x_2 = open(bpy.path.abspath("//x_2.txt"),'r').read().split('\n')
r = open(bpy.path.abspath("//r.txt"),'r').read().split('\n')
outer_fibre_diameter = 40
inner_fibre_diameter = range(3,15,1)
Cp = 0.001
w = 80
L = 40
L_inner = 100
length_fibres = 1600
N = len(x_1) - 1
N_inner = len(r) - 1 

## Creates a single cylinder with a specified position, rotation and scale ##
def create_cylinder(position = [0,0,0], rotation = [0,0,0], scale = [0.01,0.01,0.3]):
    
    bpy.ops.mesh.primitive_cylinder_add()
    so = bpy.context.active_object
    
    ## Define the rotation of the cylinder ##
    so.rotation_euler[0] += rotation[0]
    so.rotation_euler[1] += rotation[1]
    so.rotation_euler[2] += rotation[2]

    ## Define the position of the cylinder ##

    so.location[0] = position[0]/my_scale
    so.location[1] = position[1]/my_scale
    so.location[2] = position[2]/my_scale

    ## Define the size of the cylinder ##
    so.scale[0] = scale[0]/my_scale
    so.scale[1] = scale[1]/my_scale
    so.scale[2] = scale[2]/my_scale

    
## Create inner fibres ##
def create_fibres_1(pos_off_set = 0):
    for i in range(int(len(x_1) - 1)):
       print(i)
       pos = [float(pos_off_set)+float(np.random.rand()*w),float(x_1[i]),float(y_1[i])]
       angle = abs(float(angles[i]))
       create_cylinder(position = pos, rotation = [angle,0,0], 
       scale = [outer_fibre_diameter/2,outer_fibre_diameter/2,length_fibres/2])
       
## Create outer fibres ##
def create_fibres_3(pos_off_set = 0):
    for i in range(int(len(x_3) - 1)):
       pos = [float(pos_off_set)+float(np.random.rand()*w),float(x_3[i]),float(y_3[i])]
       angle = abs(float(angles[i]))
       create_cylinder(position = pos, rotation = [angle,0,0], 
       scale = [outer_fibre_diameter/2,outer_fibre_diameter/2,length_fibres/2])       
   
## Create filtering fibres ##
def create_inner_fibres(pos_off_set = 40):
    for i in range(N_inner):
       random_num = float(r[i])
       create_cylinder(position = [float(pos_off_set)+float(np.random.rand()*w),float(x_2[i]),float(y_2[i])], rotation = [float(angles[i]),0,0], 
       scale = [random_num,random_num,length_fibres/2])
   


## Create all the layers with a specific offset ##
create_fibres_1(pos_off_set = -65)
create_fibres_3(pos_off_set = 100)
create_inner_fibres()
