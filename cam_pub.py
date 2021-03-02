#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

#criando a captura
videoIn = 0 # visualizado no ls /dev
cap = cv2.VideoCapture(videoIn)

def pub_msgs():
    pub = rospy.Publisher("camera_frames", Image, queue_size=10)
    rospy.init_node("camera_pub", anonymous=True)

    rate = rospy.Rate(10)

    cap_video = cv2.VideoCapture(videoIn)

    bridge = CvBridge()

    while not rospy.is_shutdown():

        ret,cv_image = cap.read()

        if ret == True:
            rospy.loginfo('Pepe, TAMO NA GLOBOOO')

            pub.publish(bridge.cv2_to_imgmsg(cv_image))

        rate.sleep()

if __name__ == '__main__':
    try:
        pub_msgs()
    except rospy.ROSInterruptException:
        pass

    


