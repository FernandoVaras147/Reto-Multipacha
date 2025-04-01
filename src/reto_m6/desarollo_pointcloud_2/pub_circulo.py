#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import std_msgs.msg
import math

def generar_puntos_circulo(radio=0.3, cantidad=50):
    puntos = []
    for i in range(cantidad):
        angulo = 2 * math.pi * i / cantidad
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        z = 0
        puntos.append([x, y, z])
    return puntos

def publicar_pointcloud():
    rospy.init_node('pub_circulo')
    pub = rospy.Publisher('/nube_entrada', PointCloud2, queue_size=10)
    rate = rospy.Rate(1)

    puntos = generar_puntos_circulo()

    while not rospy.is_shutdown():
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = "map"

        nube = pc2.create_cloud_xyz32(header, puntos)
        pub.publish(nube)
        rate.sleep()

if __name__ == "__main__":
    publicar_pointcloud()
