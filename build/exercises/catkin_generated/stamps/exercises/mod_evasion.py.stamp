#!/usr/bin/env python3

# %%  Librerias

import rospy
import numpy_ros as ros_numpy
import numpy as np
import mod_laser as ml
import smach
import math


# %% Funciones


# %% Clases

class scan(object):
    """ Clase para el manejo de evasion del robot"""
    
    def __init__(self, laser, lectura_max):
        self.laser = laser   
        self.lectura_max = lectura_max
        
    def get_lectura_cuant(self):
    	data = self.laser.get_data()
    	lectura = np.asarray(data.ranges) # convierte la info en arreglo numpy
    	lectura = np.where(lectura>self.lectura_max, self.lectura_max, lectura) #remove infinito

    	right_scan=lectura[:230]   # discrimina por direccion
    	left_scan=lectura[492:]
    	front_scan=lectura[230:492]

    	sr = 0
    	sl = 0
    	sf =0
    	# promedia valores y cuantiza
    	if np.mean(left_scan)< 3: 
    		sl=1 
        else:
            sl = 0
    	if np.mean(right_scan)< 3: 
    		sr=1
        else:
            sl = 0
    	f np.mean(front_scan)< 3: 
    		sf=1	
        else:
            sr = 0            
    	return sl,sf,sr   
     
    def free_access()
        data = self.laser.get_data()
    	lectura = np.asarray(data.ranges) # convierte la info en arreglo numpy
    	lectura = np.where(lectura>self.lectura_max, self.lectura_max, lectura) #remove infinito 
        p = np.arange(0,721)
        i = -2.0999999046325684 
        for angles_all in p:
            angles_all=i
            i=i+0.005833333358168602
         p=0   
        robot_width = 5
        for free_access in p:
            free_access =  robot_width/(2*np.sin(angles_all[i]))
            p=p+1
    return  free_access, angles_all