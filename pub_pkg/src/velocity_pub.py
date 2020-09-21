#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3

rospy.init_node('velocity_pub_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)

while not rospy.is_shutdown(): 
    linear_x = 0.5
    angular_z = 0.5
    var = Twist(Vector3(linear_x,0,0),Vector3(0,0,angular_z))
    pub.publish(var)
    rate.sleep()