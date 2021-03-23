#!/usr/bin/env python  
import rospy

from message.msg import cus_msg

def main():
   rospy.init_node("mymsg_publisher")
   pub = rospy.Publisher("mymsg", cus_msg, queue_size=1)
   r=rospy.Rate(1)
   
   msg = cus_msg()
   while not rospy.is_shutdown():
      msg.a = 5
      msg.b = 6
      pub.publish(msg)
      r.sleep()

if __name__ =="__main__":
   try:
      main()
   except rospy.ROSInterruptException:
      pass  

