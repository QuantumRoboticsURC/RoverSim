#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Twist, Pose2D

class DifferentialDriveModel:
    
    def __init__(self):
        rospy.init_node('differential_drive_model')
        self.twist_sub = rospy.Subscriber('/cmd_vel', Twist, self.twist_callback)
        self.puzzlebot_pose_sub = rospy.Subscriber('/pose', Pose2D, self.pose_callback)
        self.puzzlebot_twist_on_base_frame_pub = rospy.Publisher('/puzzlebot_vel_on_base_frame_pub', Twist, queue_size=1)
        self.puzzlebot_twist_on_base_frame = Twist()
        self.puzzlbeot_pose_th = None
        self.twist_linear_x = None
        self.twist_angular_z = None
        self.rate = rospy.Rate(10.0)

    def pose_callback(self, msg):
        self.puzzlbeot_pose_th = msg.theta

    def twist_callback(self, msg):
        self.twist_linear_x = msg.linear.x
        self.twist_angular_z = msg.angular.z        

    def main(self):
        while not rospy.is_shutdown():
            if self.puzzlbeot_pose_th is not None and self.twist_linear_x is not None and self.twist_angular_z is not None:
                self.puzzlebot_twist_on_base_frame.linear.x = self.twist_linear_x*np.cos(self.puzzlbeot_pose_th)
                self.puzzlebot_twist_on_base_frame.linear.y = self.twist_linear_x*np.sin(self.puzzlbeot_pose_th)
                self.puzzlebot_twist_on_base_frame.angular.z = self.twist_angular_z
                self.puzzlebot_twist_on_base_frame_pub.publish(self.puzzlebot_twist_on_base_frame)
            self.rate.sleep()

if __name__ == '__main__':
    ddm = DifferentialDriveModel()
    ddm.main()