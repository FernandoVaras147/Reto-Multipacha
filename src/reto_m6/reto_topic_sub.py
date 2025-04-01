#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Mensaje recibido: %s", data.data)

def main():
    rospy.init_node('subscriber_node')
    rospy.Subscriber('reto_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
