#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64,Int16,String

def main(data):
    
    rospy.loginfo(" op: %d " , data.data )

def listener():
    rospy.init_node('final_subscriber', anonymous=True)
    rospy.Subscriber("final", Int16, main)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()