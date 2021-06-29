import numpy as np
import matplotlib.pyplot as plt
import random 
import os

## Define parameters ##
length = 2000
mesh_domain = 200
inner_packing = 0.2
outer_packing = 0.4


## Open text files to write to ##
x_1data = open('x_1.txt','w')
y_1data = open('y_1.txt','w')
x_2data = open('x_2.txt','w')
y_2data = open('y_2.txt','w')
x_3data = open('x_3.txt','w')
y_3data = open('y_3.txt','w')
r = open('r.txt','w')
x_1data.write('')
y_1data.write('')
x_2data.write('')
y_2data.write('')
x_3data.write('')
r.write('')
y_3data.write('')
x_1data.close()
y_1data.close()
x_2data.close()
y_2data.close()
x_3data.close()
y_3data.close()


## Detects the intersection between the fibres and the domain and returns the new fibre length##
def plot_lines(x,y,angle):
    r1 = [x+(length/2)*np.sin(angle),y+(length/2)*np.cos(angle)]
    r2 = [x-(length/2)*np.sin(angle),y-(length/2)*np.cos(angle)]
    m,b = np.polyfit([r1[0],r2[0],x],[r1[1],r2[1],y],1)


    plt.plot([r1[0],r2[0]],[r1[1],r2[1]], color = 'black')
    plt.xlim(-mesh_domain-100,mesh_domain+100)
    plt.ylim(-mesh_domain-100, mesh_domain+100)
    
    
    if angle <= np.radians(45) and (mesh_domain-b)/m < mesh_domain and (-mesh_domain-b)/m > -mesh_domain:

        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
    elif angle <= np.radians(45) and (mesh_domain-b)/m > mesh_domain:
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = mesh_domain
        y2 = mesh_domain*m + b
        
    elif angle <= np.radians(45) and (-mesh_domain-b)/m < -mesh_domain:
        x1 = -mesh_domain
        y1 = -mesh_domain*m + b
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
        
    if np.radians(45) < angle <= np.radians(135) and -mesh_domain*m + b > -mesh_domain and m*mesh_domain + b > -mesh_domain and -mesh_domain*m + b < mesh_domain and m*mesh_domain + b < mesh_domain:

        x1 = mesh_domain
        y1 = m*mesh_domain + b
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b
        
    elif np.radians(45) < angle <= np.radians(135) and -mesh_domain*m + b < -mesh_domain:
        
        x1 = mesh_domain
        y1 = m*mesh_domain + b
        
        
        x2 = (-mesh_domain-b)/m
        y2 = -mesh_domain
        
    elif np.radians(45) < angle <= np.radians(135) and m*mesh_domain + b < -mesh_domain:

        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b
        
    elif np.radians(45) < angle <= np.radians(135) and m*mesh_domain + b > mesh_domain:

        x1 = (mesh_domain-b)/m
        y1 = mesh_domain
        
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b    
        
    elif np.radians(45) < angle <= np.radians(135) and -mesh_domain*m + b > mesh_domain:

        x1 = (mesh_domain-b)/m
        y1 = mesh_domain
        
        
        x2 = mesh_domain
        y2 = mesh_domain*m + b
        
    
    
    if np.radians(135) < angle < np.radians(225) and (mesh_domain-b)/m > -mesh_domain and (mesh_domain-b)/m < mesh_domain and (-mesh_domain-b)/m < mesh_domain and (-mesh_domain-b)/m > -mesh_domain:
        print('yes')
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
    elif np.radians(135) < angle < np.radians(225) and (mesh_domain-b)/m > mesh_domain:
    
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = mesh_domain
        y2 = mesh_domain*m+b
        
    elif np.radians(135) < angle < np.radians(225) and (mesh_domain-b)/m < -mesh_domain:
    
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m+b
        
    elif np.radians(135) < angle < np.radians(225) and (-mesh_domain-b)/m > mesh_domain:
       
        x1 = mesh_domain
        y1 = mesh_domain*m+b
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
    elif np.radians(135) < angle < np.radians(225) and (-mesh_domain-b)/m < -mesh_domain:
  
        x1 = -mesh_domain
        y1 = -mesh_domain*m + b
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
        
    if np.radians(225) <= angle < np.radians(315)  and mesh_domain > m*mesh_domain + b > -mesh_domain and -mesh_domain*m + b < mesh_domain and -mesh_domain*m + b > -mesh_domain:

        x1 = mesh_domain
        y1 = m*mesh_domain + b
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b
        
    elif np.radians(225) <= angle < np.radians(315)  and m*mesh_domain + b < -mesh_domain:
        
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b
        
    elif np.radians(225) <= angle < np.radians(315)  and -mesh_domain*m + b > mesh_domain:
  
        x1 = mesh_domain
        y1 = mesh_domain*m + b
        
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
    
    elif np.radians(225) <= angle < np.radians(315)  and -mesh_domain*m + b < -mesh_domain:

        x1 = mesh_domain
        y1 = mesh_domain*m + b
        
        
        x2 = (-mesh_domain-b)/m
        y2 = -mesh_domain
        
    elif np.radians(225) <= angle < np.radians(315)  and m*mesh_domain + b > mesh_domain:

        x1 = (mesh_domain-b)/m
        y1 = mesh_domain
        
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b
        
    if  np.radians(315) <= angle and (-mesh_domain-b)/m < mesh_domain and (mesh_domain-b)/m > -mesh_domain:
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
    elif np.radians(315) <= angle and (-mesh_domain-b)/m > mesh_domain:
        x1 = mesh_domain
        y1 = mesh_domain*m + b
        
        x2 = (mesh_domain-b)/m
        y2 = mesh_domain
        
    elif np.radians(315) <= angle  and (mesh_domain-b)/m < -mesh_domain:
        x1 = (-mesh_domain-b)/m
        y1 = -mesh_domain
        
        x2 = -mesh_domain
        y2 = -mesh_domain*m + b
    
        
    
    plt.scatter([x1],[y1], color = 'black')
    plt.scatter(x2,y2, color = 'black')
    
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


## Create filter layer ##
def create_filter():
    ## Declaration of variables ##
    inner_fibre_diameter = range(3,15,1)
    vol = 0
    i = 0
    
    ## Begin main loop ##
    while vol < inner_packing:
        
        ## Define the total volume and open required text files ##
        total_volume = 80*400*400
        x_data = open('x_2.txt','a')
        y_data = open('y_2.txt','a')
        r = open('r.txt','a')
        angles = open("Cp001.txt",'r').read().split('\n')
        
        ## Create all random numbers ##
        random_num = random.choice(inner_fibre_diameter)/2
        y = random.choice((-1, 1))*float(np.random.rand()*mesh_domain)
        x = random.choice((-1, 1))*float(np.random.rand()*mesh_domain)   
        angle = abs(float(angles[i]))
        
        ## Write the data to a text file ##
        x_data.write(str(x)+'\n')
        y_data.write(str(y)+'\n')
        r.write(str(random_num)+'\n')
        r.close()
        x_data.close()
        y_data.close()
        
        ## Determine the new length and calculate the new volume, 
        ## count the amount of fibres with variable i
        new_length = plot_lines(x,y,angle = angle)
        volume = ((np.pi*(random_num**2))*new_length)/total_volume
        vol = vol + volume
        i = i + 1


## Creates the ouer fibres ##
def create_outer():
    vol = 0
    i = 0
    while vol < outer_packing:
        total_volume = 80*400*400
        x_data = open('x_3.txt','a')
        y_data = open('y_3.txt','a')
        #r = open('r.txt','a')
        random_num = 20
        angles = open("Cp001.txt",'r').read().split('\n')
        y = random.choice((-1, 1))*float(np.random.rand()*mesh_domain)
        x = random.choice((-1, 1))*float(np.random.rand()*mesh_domain)   
        x_data.write(str(x)+'\n')
        y_data.write(str(y)+'\n')

        x_data.close()
        y_data.close()
        angle = abs(float(angles[i]))
        print(x,y,np.degrees(angle))
        new_length = plot_lines(x,y,angle = angle)
        print(new_length)
        volume = ((np.pi*(random_num**2))*new_length)/total_volume
        vol = vol + volume
        i = i+1
        
## Create the fibres facing the face of the individual ##
def create_inner():
    vol = 0
    i = 0
    while vol < outer_packing:
        total_volume = 80*400*400
        x_data = open('x_1.txt','a')
        y_data = open('y_1.txt','a')
        #r = open('r.txt','a')
        random_num = 20
        angles = open("Cp001.txt",'r').read().split('\n')
        y = random.choice((-1, 1))*float(np.random.rand()*mesh_domain)
        x = random.choice((-1, 1))*float(np.random.rand()*mesh_domain)   
        x_data.write(str(x)+'\n')
        y_data.write(str(y)+'\n')
        x_data.close()
        y_data.close()
        angle = abs(float(angles[i]))
        print(x,y,np.degrees(angle))
        new_length = plot_lines(x,y,angle = angle)
        print(new_length)
        volume = ((np.pi*(random_num**2))*new_length)/total_volume
        vol = vol + volume
        i = i+1
        
## Create each layer ##
create_inner()
create_filter()
create_outer()


    


