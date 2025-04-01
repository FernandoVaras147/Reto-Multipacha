#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import std_msgs.msg
import numpy as np

def calcular_centro_y_radio(puntos):
    puntos_np = np.array(puntos)
    centro = np.mean(puntos_np[:, :2], axis=0)

    # Calcular el lado estimado del cuadrado
    max_x, min_x = np.max(puntos_np[:, 0]), np.min(puntos_np[:, 0])
    max_y, min_y = np.max(puntos_np[:, 1]), np.min(puntos_np[:, 1])
    lado_estimado = max(max_x - min_x, max_y - min_y)

    radio = lado_estimado*0.9 / 2
    return centro, radio

def filtrar_puntos(puntos, centro, radio):
    filtrados = []
    for x, y, z in puntos:
        distancia = np.sqrt((x - centro[0])**2 + (y - centro[1])**2)
        # Solo puntos estrictamente en el círculo o dentro
        if distancia <= radio:
            filtrados.append([x, y, z])
    return filtrados

def callback_pointcloud(msg):
    puntos = list(pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True))
    if not puntos:
        return

    centro, radio = calcular_centro_y_radio(puntos)
    puntos_filtrados = filtrar_puntos(puntos, centro, radio)

    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = "map"

    nube_filtrada = pc2.create_cloud_xyz32(header, puntos_filtrados)
    pub_resaltado.publish(nube_filtrada)

def main():
    rospy.init_node("resaltar_circulo_preciso")
    rospy.Subscriber("/nube_entrada", PointCloud2, callback_pointcloud)
    global pub_resaltado
    pub_resaltado = rospy.Publisher("/nube_resaltada", PointCloud2, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
