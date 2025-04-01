#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import String
import math
import numpy as np

def calcular_distancias(puntos):
    puntos_np = np.array(puntos)
    centro = np.mean(puntos_np, axis=0)
    distancias = np.linalg.norm(puntos_np[:, :2] - centro[:2], axis=1)
    return sorted(distancias), centro

def clasificar_figura(distancias):
    tolerancia_circulo = 0.01
    distancias = np.array(distancias)

    # Verificamos si todas las distancias son casi iguales → círculo
    if np.std(distancias) < tolerancia_circulo:
        return "circulo"

    # Excluir las 4 distancias más grandes (esquinas)
    if len(distancias) > 8:
        distancias_sin_esquinas = distancias[:-4]
        valores, conteos = np.unique(np.round(distancias_sin_esquinas, 2), return_counts=True)
        if all(c % 4 == 0 for c in conteos):
            return "cuadrado"

    return "ninguno"

def callback_pointcloud(msg):
    puntos = list(pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True))
    distancias, _ = calcular_distancias(puntos)
    figura = clasificar_figura(distancias)
    rospy.loginfo(f"Figura detectada: {figura}")
    publicador_resultado.publish(String(data=figura))

if __name__ == "__main__":
    rospy.init_node("detector_figura")
    publicador_resultado = rospy.Publisher("/resultado_figura", String, queue_size=10)
    rospy.Subscriber("/nube_entrada", PointCloud2, callback_pointcloud)
    rospy.spin()
