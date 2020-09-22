#! /usr/bin/env python

import rospy
# need to import rospkg to use rospack.get_path
import rospkg
# Import the service message used by the service /trajectory_by_name
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

rospy.init_node('robot_arm_node')
rospy.wait_for_service('/execute_trajectory')
exec_traj_srv = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
exec_traj_obj = ExecTrajRequest()

rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory')+"/config/get_food.txt"

exec_traj_obj.file = traj
result = exec_traj_srv(exec_traj_obj)
print result    # Print the result given by the service called
