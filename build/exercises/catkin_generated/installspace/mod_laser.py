#!/usr/bin/env python3
"""
Fecha  23/08/2022  17:51 p.m

@author: Oviedo Martin

GMail: eliasoviedo1718@gmail.com


 Resumen :
   Modulo para el manejo del laser del robot TAKESHI.


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


import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
import numpy_ros as ros_numpy


# %% Funciones


# %% Clases

class laser(object):
    """Clase para el manejo del Laser"""

    def __init__(self):
        #Registre el método _laser_cb como una devolución de llamada a los eventos del tema de escaneo láser
        self._laser_sub = rospy.Subscriber('/hsrb/base_scan', LaserScan, self._laser_cb)
        self._scan_data = None

    def _laser_cb(self, msg):
        #Laser scan callback function
        self._scan_data = msg

    def get_data(self):
        #Function to get the laser value
        return self._scan_data   
            

