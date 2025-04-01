#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import std_msgs.msg
import numpy as np

def generar_puntos_triangulo_contorno(puntos_por_lado=20, lado=1.0):
    puntos = []

    # Vértices del triángulo equilátero
    A = np.array([0, 0])
    B = np.array([lado, 0])
    C = np.array([lado / 2, (np.sqrt(3)/2) * lado])  # Altura

    # Lado AB
    for i in range(puntos_por_lado):
        t = i / (puntos_por_lado - 1)
        punto = (1 - t) * A + t * B
        puntos.append([punto[0], punto[1], 0])

    # Lado BC
    for i in range(puntos_por_lado):
        t = i / (puntos_por_lado - 1)
        punto = (1 - t) * B + t * C
        puntos.append([punto[0], punto[1], 0])

    # Lado CA
    for i in range(puntos_por_lado):
        t = i / (puntos_por_lado - 1)
        punto = (1 - t) * C + t * A
        puntos.append([punto[0], punto[1], 0])

    return puntos

def publicar_pointcloud():
    rospy.init_node('pub_triangulo')
    pub = rospy.Publisher('/nube_entrada', PointCloud2, queue_size=10)
    rate = rospy.Rate(1)

    puntos = generar_puntos_triangulo_contorno()

    while not rospy.is_shutdown():
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = "map"

        nube = pc2.create_cloud_xyz32(header, puntos)
        pub.publish(nube)
        rate.sleep()

if __name__ == "__main__":
    publicar_pointcloud()
