import rospy
from datetime import datetime
import time
from datetime import timedelta
from gpiozero import Button, LED
from std_msgs.msg import Int16

id = 2
start = 0
status = 0
Input= Button(4)

rospy.init_node('Smart_sensor',anonymous=True)
pub = rospy.Publisher('sensorStatId', Int16, queue_size=10)

print("Sensor is READY")
while not rospy.is_shutdown():
    if not Input.is_pressed:
        if time.time() - start < 1:
            status = 1
        else:
            status = 0
        start = time.time()
        while not Input.is_pressed:
            if time.time() - start > 0.02:
                status = 2
                break

        msg = status * 100 + id
        print(msg)
        pub.publish(msg)
        
