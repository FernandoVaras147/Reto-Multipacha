**Desarrollo para ROS**

Parte 1

Manejo de directorios y paquetes

- Se creó un workspace llamado `multipacha_ws`
- Se creó el paquete `reto_m6` con las dependencias: `rospy`, `rviz`, `sensor_msgs`, `std_msgs`

Tópicos publicadores y suscriptores

- `reto_topic_pub.py`: Publica el mensaje `"M6 Reto"` al tópico `/m6_topic` a 10 Hz
- `reto_topic_sub.py`: Se suscribe a `/m6_topic` e imprime los mensajes en consola

Modelado URDF

- El modelo `reto_robot.urdf` representa un robot con dos cilindros unidos por una junta `revolute`
- Se encuentra en el directorio: `urdf/`

Archivos Launch

Ubicados en `launch/`:

- `pub.launch`: Lanza el nodo `reto_topic_pub.py`
- `sub.launch`: Lanza el nodo `reto_topic_sub.py` con `output="screen"`
- `robot.launch`: Lanza RViz, el modelo URDF y `joint_state_publisher_gui` para interactuar con la junta

Parte 2

Esta parte se enfocó en aplicar procesamiento sobre datos de sensores simulados (nubes de puntos) dentro del entorno ROS. Todo se encuentra en el directorio `desarrollo_pointcloud/`.

---

**Desarrollo para PointCloud**

Parte 1:

Generación de figuras geométricas

Scripts en `desarollo_pointcloud_2/` que publican nubes de puntos (`PointCloud2`) en el tópico `/nube_entrada`:

- `pub_cuadrado.py`: Genera un cuadrado - contorno
- `pub_circulo.py`: Genera un círculo - contorno
- `pub_triangulo.py`: Genera un triángulo - contorno

Detección de figuras

- `detector_figura.py`: Detecta si la nube en `/nube_entrada` corresponde a un **cuadrado**, **círculo** o **figura no determinada**.
- Analiza distancias desde el centro al resto de puntos
- Resultado se publica en `/resultado_figura` como `std_msgs/String`

Parte 2:

Generacion de la malla de puntos

Scripts en `desarollo_pointcloud_2/` que publican nubes de puntos (`PointCloud2`) en el tópico `/nube_entrada`:

- `pub_malla.py`: Genera un cuadrado relleno

Resaltado visual de círculo

- `resaltar_circulo.py`: Similar al filtro, pero resalta puntos que **pertenecen al círculo** original (con precisión), publicándolos en `/nube_resaltada`

