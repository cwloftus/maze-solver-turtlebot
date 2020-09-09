#!/bin/bash

echo "Changing directory to my_scripts"
cd ~/catkin_ws/src/linux_course_files/move_bb8_pkg/my_scripts
echo "Listing folder contents with permissions"
ls -la
echo "Changing permissions"
chmod 777 move_bb8_square.py
ls -la
