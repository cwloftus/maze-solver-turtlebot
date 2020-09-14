#include <geometry_msgs/Twist.h>
#include <ros/ros.h>

int main(int argc, char **argv) {

  ros::init(argc, argv, "bot_move");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("cmd_vel", 1000);
  ros::Rate loop_rate(2);

  geometry_msgs::Twist float64;
  float64.x = 0;
  float64.y = 0.5;
  float64.z = 0.5;

  return 0;
}
