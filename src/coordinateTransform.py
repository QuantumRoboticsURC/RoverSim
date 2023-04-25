#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Pose2D
from std_msgs.msg import Float32
import tf

class CoordinateTransform:
    
    def __init__(self):
        rospy.init_node('coordinate_transform')
        self.transform_broadcaster = tf.TransformBroadcaster()
        self.puzzlebot_pose_sub = rospy.Subscriber('/pose', Pose2D, self.pose_callback)
        self.puzzlebot_pose_x = None
        self.puzzlebot_pose_y = None
        self.puzzlebot_pose_theta = None   

        self.rate = rospy.Rate(10.0)            

    def pose_callback(self, msg):
        self.puzzlebot_pose_x = msg.x
        self.puzzlebot_pose_y = msg.y
        self.puzzlebot_pose_theta = msg.theta

    def main(self):
        while not rospy.is_shutdown():
            if self.puzzlebot_pose_x is not None and self.puzzlebot_pose_y is not None and self.puzzlebot_pose_theta is not None:
                
                self.transform_broadcaster.sendTransform((self.puzzlebot_pose_x, self.puzzlebot_pose_y, 0.0),
                                tf.transformations.quaternion_from_euler(0, 0, self.puzzlebot_pose_theta),
                                rospy.Time.now(),
                                "base_link",
                                "map")
                
            self.rate.sleep()

if __name__ == '__main__':
    instance = CoordinateTransform()
    instance.main()