#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import std_msgs.msg
import struct

def publish_pointcloud():
    rospy.init_node('pointcloud_pub')
    pub = rospy.Publisher('reto_pointcloud', PointCloud2, queue_size=1)
    rate = rospy.Rate(1)

    points = []
    for x in range(-5, 6):
        for y in range(-5, 6):
            z = 0
            points.append([x * 0.1, y * 0.1, z])  

    while not rospy.is_shutdown():
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = "map"

        cloud = pc2.create_cloud_xyz32(header, points)
        pub.publish(cloud)
        rate.sleep()

if __name__ == '__main__':
    publish_pointcloud()
