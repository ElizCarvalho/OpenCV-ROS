#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def cap_img():
    path = r'/home/starwars/Downloads/by.png'
    img = cv2.imread(path)

    return img
    # cv2.imshow('image', img)
    # cv2.waitKey(0)    

def pub_msgs():
    pub = rospy.Publisher("camera_frames", Image, queue_size=10)
    rospy.init_node("camera_pub", anonymous=True)

    rate = rospy.Rate(10)

    bridge = CvBridge()

    while not rospy.is_shutdown():

        cap_image = cap_img()
        
        rospy.loginfo('Pepe, TAMO NA GLOBOOO')

        pub.publish(bridge.cv2_to_imgmsg(cap_image))

        rate.sleep()

if __name__ == '__main__':
    pub_msgs()
