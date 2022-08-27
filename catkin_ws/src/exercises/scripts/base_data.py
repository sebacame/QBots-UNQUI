#!/usr/bin/env python3
#external library
import math
import cmath
import numpy as np
import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
import tf
import tf2_ros 
#local library

rospy.init_node('base_and_sensor')    ### Conectamos/creamos un nodo llamado base and sensor 
###########################################################################################3
tfBuffer = tf2_ros.Buffer()
istener = tf2_ros.TransformListener(tfBuffer)

def get_coords ():
    for i in range(10):   ###Tcargo la posicion del centro del robot
        try:
            trans = tfBuffer.lookup_transform('map', 'base_link', rospy.Time(), rospy.Duration(2.0))
            return trans
        except:
            print ('waiting for tf')
            trans=0
def base_angle():# esto lo hago para pasar de quaterniones a angulos y asi conocer el angulo de rotacion actual del robot
    quaternion = (
    get_coords().transform.rotation.x,
    get_coords().transform.rotation.y,
    get_coords().transform.rotation.z,
    get_coords().transform.rotation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    roll = euler[0]
    pitch = euler[1]
    yaw = euler[2]
    angle_utility = round(yaw,2)
    return angle_utility
    
