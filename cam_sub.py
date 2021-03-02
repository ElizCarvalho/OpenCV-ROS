#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def callback(data):
    bridge = CvBridge()

    rospy.loginfo("WandaVision")

    cv_image = bridge.imgmsg_to_cv2(data)

    cv2.imshow("camera", cv_image)

    cv2.waitKey(1)


def receive_message():
    rospy.init_node("camera_sub", anonymous=True)

    rospy.Subscriber("camera_frames", Image, callback)

    rospy.spin()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        receive_message()
    except rospy.ROSInterruptException:
        pass
