#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('publisher_node')
    pub = rospy.Publisher('reto_topic', String, queue_size=10)
    rate = rospy.Rate(10)  

    while not rospy.is_shutdown():
        mensaje = "M6 Reto"
        rospy.loginfo(mensaje)
        pub.publish(mensaje)
        rate.sleep()

if __name__ == '__main__':
    main()
