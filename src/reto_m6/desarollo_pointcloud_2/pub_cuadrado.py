#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import std_msgs.msg

def generar_puntos_cuadrado_contorno(lado=7, paso=0.1):
    puntos = []
    for i in range(lado):
        for j in range(lado):
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                x = i * paso
                y = j * paso
                z = 0
                puntos.append([x, y, z])
    return puntos

def publicar_pointcloud():
    rospy.init_node('pub_cuadrado_contorno')
    pub = rospy.Publisher('/nube_entrada', PointCloud2, queue_size=10)
    rate = rospy.Rate(1)

    puntos = generar_puntos_cuadrado_contorno()

    while not rospy.is_shutdown():
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = "map"

        nube = pc2.create_cloud_xyz32(header, puntos)
        pub.publish(nube)
        rate.sleep()

if __name__ == "__main__":
    publicar_pointcloud()

