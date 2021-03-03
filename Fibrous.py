import numpy as np
import random 
import math 
import bpy



domain_cross_section = 200


inner_alpha = 1.5
outer_alpha = 4
angles = open(bpy.path.abspath("//Cp001.txt"),'r').read().split('\n')
outer_fibre_diameter = 40
inner_fibre_diameter = range(3,15,1)
Cp = 0.001
w = 800
L = 40
L_inner = 100
length_fibres = 1600
N = (4*outer_alpha*L*w**2)/(length_fibres*np.pi*outer_fibre_diameter**2)
N_inner = (4*inner_alpha*L*w**2)/(length_fibres*np.pi*8**2)


def create_cylinder(position = [0,0,0], rotation = [0,0,0], scale = [0.01,0.01,0.3]):
    
    bpy.ops.mesh.primitive_cylinder_add()
    so = bpy.context.active_object

    ## Define the position of the cylinder ##

    so.location[0] = position[0]/1000
    so.location[1] = position[1]/1000
    so.location[2] = position[2]/1000

    ## Define the rotation of the cylinder ##
    so.rotation_euler[0] += rotation[0]
    so.rotation_euler[1] += rotation[1]
    so.rotation_euler[2] += rotation[2]


    ## Define the size of the cylinder ##
    so.scale[0] = scale[0]/1000
    so.scale[1] = scale[1]/1000
    so.scale[2] = scale[2]/1000
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object =    bpy.data.objects["Cube"]
    bpy.ops.object.modifier_apply(modifier="Boolean")
    

def create_fibres(pos_off_set = 0):
    for i in range(int(N)):
       create_cylinder(position = [float(pos_off_set)+float(np.random.rand()*L),
       random.choice((-1, 1))*float(np.random.rand()*w/2),
       random.choice((-1, 1))*float(np.random.rand()*w/2)], rotation = [float(angles[i]),0,0], 
       scale = [outer_fibre_diameter/2,outer_fibre_diameter/2,length_fibres/2])
   
 
def create_inner_fibres(pos_off_set = 40):
    for i in range(int(N_inner)):
       random_num = random.choice(inner_fibre_diameter)
       create_cylinder(position = [float(pos_off_set)+float(np.random.rand()*L_inner),
       random.choice((-1, 1))*float(np.random.rand()*w/2),
       random.choice((-1, 1))*float(np.random.rand()*w/2)], rotation = [float(angles[i]),0,0], 
       scale = [random_num/2,random_num/2,length_fibres/2])
   

def create_cube(): 
    bpy.ops.mesh.primitive_cube_add()
    so = bpy.context.active_object
    so.scale[0] = L/1000
    so.scale[1] = 8*w/1000
    so.scale[2] = 8*w/1000
    so.location[0] = L/2000
    so.location[1] = 0
    so.location[2] = 0

    bpy.ops.mesh.primitive_cube_add()
    so = bpy.context.active_object
    so.scale[0] = L/1000
    so.scale[1] = domain_cross_section/1000
    so.scale[2] = domain_cross_section/1000
    so.location[0] = L/2000
    so.location[1] = 0
    so.location[2] = 0

create_fibres(pos_off_set = 0)
create_fibres(pos_off_set = 160)
create_inner_fibres()
