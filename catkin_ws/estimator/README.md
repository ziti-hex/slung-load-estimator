# ROS Package
Hier ist die Dateistruktr einer ROS-Package
## estimator.launch
Startet mavros und VideoStream nodes unter ROS dient etwas automatisierung des Aufrufs der benötigten Nodes unter ROS. Ohne dieser Datei muss man aufrufen:  
roslaunch mavros px4.launch baud url   
roslaunch viedeo_stream_opencv camera.launch  
Der Aufruf:
roslaunch estimator estimator.launch  
startet beide Nodes video und mavros mit oreingestellten Parametern wie Bauds, Url's, /dev/   
