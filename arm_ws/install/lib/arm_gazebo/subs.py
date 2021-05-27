#!/usr/bin/env python3
import rospy
from std_msgs import msg
from std_msgs.msg import Int64
from beginner_tutorials.msg import RotationTranslationInput
from beginner_tutorials.msg import RotationTranslationOutput
class Echo(object):
    def __init__(self):
        self.value=0
        rospy.init_node("echoer2")
        
        rospy.Subscriber("out_value",RotationTranslationOutput,self.update_value)
        rospy.spin()
    def update_value(self,msg):
        self.value=msg
        rospy.loginfo(self.value)
    def run(self):
        r=rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(self.value+3)
            r.sleep()
if __name__ == '__main__':
    try:
        Echo()
    except rospy.ROSInterruptException: pass