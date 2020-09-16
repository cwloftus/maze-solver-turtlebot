#include <nav_msgs/Odometry.h>
#include <ros/ros.h>
#include <std_msgs/Int32.h>

void odomCallback(const nav_msgs::Odometry::ConstPtr &msg) {
  ROS_INFO("%s", msg->header.frame_id.c_str());
  ROS_INFO("%f", msg->twist.twist.linear.x);
  ROS_INFO("%f", msg->twist.twist.linear.z);
}

int main(int argc, char **argv) {

  ros::init(argc, argv, "odom_subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("odom", 1000, odomCallback);

  ros::spin();

  return 0;
}
