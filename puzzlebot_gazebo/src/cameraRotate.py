#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
import rospy
from std_msgs.msg import Bool, String
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist, Pose2D
import cv2 as cv
import cv_bridge

#Creamos la clase
class cameraRotor():
    def __init__(self):
        #Inicializamos el nodo
        rospy.init_node("cameraRotor")
        #Creamos el publisher
        self.pub = rospy.Publisher("/camera/image_rotated", Image, queue_size=1)        
        
        #Creamos los subscribers
        self.imageSubscriber = rospy.Subscriber("/camera/image_raw",Image,self.on_image_callback)

        self.bridge = cv_bridge.CvBridge()   

        self.image = None   

        self.cv_image = np.zeros((300,300, 3))        
        self.outImage = np.zeros((300,280, 3))

        self.cv_image = np.uint8(self.cv_image)
        self.outImage = np.uint8(self.outImage)
        
        #Declaramos que vamos a mandar 20 mensajes por segundo.
        self.rate = rospy.Rate(30)
        self.rateInt = 30
        self.msg = Twist()
        self.processed_image_msg = Image()

        #Creamos un función de que hacer cuando haya un shutdown        
        rospy.on_shutdown(self.end_callback)

    def on_image_callback(self, image):
        self.image = image        

    def end_callback(self):
        """Funcion que para el puzzlebot cuando el nodo deja de ser corrido"""
        #Declaramos las velocidades de cero
        self.msg.linear.x = 0.0
        self.msg.angular.z = 0.0
        #Publicamos las velocidades
        self.pub.publish(self.msg)

    def main(self):
        while not rospy.is_shutdown():
            try:
                if self.image != None:
                    self.cv_image = self.bridge.imgmsg_to_cv2(self.image, desired_encoding="bgr8")
                    self.outImage = cv.rotate(self.cv_image,cv.ROTATE_180) 
                    self.processed_image_msg = self.bridge.cv2_to_imgmsg(self.outImage, encoding = "bgr8")
                    self.pub.publish(self.processed_image_msg)
                self.rate.sleep()
            except rospy.ROSTimeMovedBackwardsException:
                rospy.logerr("ROS Time Backwards! Just ignore the exception!")


#Si el archivo es corrido directametne y no llamado desde otro archivo corremos

if __name__ == "__main__":
    node = cameraRotor()
    node.main()
