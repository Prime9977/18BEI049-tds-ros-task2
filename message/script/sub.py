#!/usr/bin/env python
import rospy
from message.msg import cus_msg

def main(data):
    y = (data.a + data.b)* 3
    rospy.loginfo("   a: %d b: %d (a+b)*3: %d" %(data.a,data.b,y))

def listener():
    rospy.init_node('mymsg_subscriber', anonymous=True)
    rospy.Subscriber("mymsg", cus_msg, main)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()