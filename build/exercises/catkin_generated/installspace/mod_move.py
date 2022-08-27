#!/usr/bin/env python3
"""
Fecha  20/08/2022  05:08 p.m

@author: Oviedo Martin

GMail: eliasoviedo1718@gmail.com


 Resumen :
   Modulo para el movimiento del robot TAKESHI


 -----------
 Referencias
 -----------

    [] 
   
 -----------
   Enlaces
 ----------- 

    [] 
    

"""
# %%  Librerias

import rospy
import numpy_ros as ros_numpy
import numpy as np
from geometry_msgs.msg import Twist

import time


# %% Funciones


# %% Clases

class move(object):
    """ Clase para el manejo de movimientos del robot"""
    
    def __init__(self, base_vel_pub):
        self.base_vel_pub = base_vel_pub   
     
        
    def move_base_vel(self, vx, vy, vw):
        twist = Twist()
        twist.linear.x = vx
        twist.linear.y = vy
        twist.angular.z = vw 
        self.base_vel_pub.publish(twist) 
               
    def move_base(self, x, y, yaw, timeout=5):        
        start_time = rospy.Time.now().to_sec()
        while rospy.Time.now().to_sec() - start_time < timeout:  
            self.move_base_vel(x, y, yaw)
            
    def move_forward(self):
        self.move_base(0.20 ,0 ,0 ,1)
        
    def move_backward(self):
        self.move_base(-0.20 ,0 ,0 ,0.1)
        
    def turn_left(self):
        self.move_base(0.1, 0, 0.15*np.pi, 0.2)

    def turn_right(self):
        self.move_base(0.1, 0, -0.15*np.pi, 0.2)             
            

