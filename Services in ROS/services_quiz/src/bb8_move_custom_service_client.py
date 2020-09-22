#! /usr/bin/env python

import rospkg
import rospy
from std_srvs.srv import Empty, EmptyRequest
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_bb8_in_square_custom_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest()

"""
# BB8CustomServiceMessage
float64 side        # The distance of each side of the square
int32 repetitions   # The number of times BB-8 has to execute the square movement when the service is called
---
bool success        # Did it achieve it?
"""

move_bb8_in_square_request_object.side = 3
move_bb8_in_square_request_object.repetitions = 2

rospy.loginfo("Starting small squares")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) 
rospy.loginfo(str(result))

move_bb8_in_square_request_object.side = 6
move_bb8_in_square_request_object.repetitions = 1

rospy.loginfo("Starting big square")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) 
rospy.loginfo(str(result))

rospy.loginfo("Finished")
