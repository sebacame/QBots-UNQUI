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
import meta_publisher as goal
import base_data as bd

#rospy.init_node('exercise01_node')
starting_coords=bd.get_coords()
starting_time=rospy.Time.now().to_sec()
meta=goal.gen_random_goal()
goal_comp_pub = rospy.Publisher('/goal', PoseStamped, queue_size=10)

rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
        goal_comp_pub.publish(meta)
        base_coords = bd.get_coords()
        goalx = meta.pose.position.x#posicion en x de la meta
        goaly = meta.pose.position.y#posicion en y de la meta
        basex = base_coords.transform.translation.x#posicion en x del robot
        basey = base_coords.transform.translation.y#posicion en y del robot
        lineal_x = goalx - basex#comparo la coordenada x del robot con la de destino
        lineal_y = goaly - basey#comparo la coordenada y del robot con la de destino
        condx=lineal_x > 0.1 or lineal_x < -0.1
        condy=lineal_y > 0.1 or lineal_y < -0.1
        condicion1 = condx  and condy   #condicion1 true si el robot no esta en la meta
        
        if not condicion1:
            ending_time=rospy.Time.now().to_sec()
            print('Tiempo recorrido: ',ending_time-starting_time)
            break
         
        rate.sleep()