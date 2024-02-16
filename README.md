Folder:
Servo - code to play around with the servo, servo.py can be used set the servo to specific angles
Sensor - code to play around with the tfmini.py starts up the sensor and we can read distances, useful for configuration
ServoSensor - the actual code that rotates the sensor with the servo, use file rig_2.py, if using this make sure you terminate programs from Servo and Sensor folder
TfMiniServer - here the file server.py gets the 2d points from rig_2.py over a socket connection. To use, start up server.py on your computer, and on the pi run rig_2.py, once rig_2.py finishes
scanning server.py will get the code and plot it. 
Note: to use server.py create a private network with the pi, making the network address 192.168.137.0, and give your host an address of 192.168.137.2. The Pi already has that network on eth0, the ethernet port, setup
Note: each folder had its own virtual env, create your own for each, or create one for every folder. You can figure out the dependeicnes from looking at the import files listed above. Socket and json packages are apart of python's standard lib.
