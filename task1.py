#!/usr/bin/env python3
import rospy



#add your publisher and subscriber functions and complete the task



if __name__ == '__main__':
    rospy.init_node("turtle_control") #initiate 
    sub=rospy.Subscriber("") #add what topic you want to subscribe to
    pub=rospy.Publisher("") #add what topic you want to publish to

    rospy.spin() 