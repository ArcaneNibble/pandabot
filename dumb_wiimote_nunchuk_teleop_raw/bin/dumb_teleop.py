#!/usr/bin/env python

import roslib; roslib.load_manifest("dumb_wiimote_nunchuk_teleop_raw")
import rospy

from joy.msg import Joy
from geometry_msgs.msg import Twist


def nunchuk_cb(msg):
	global pub
	#print msg
	
	cmd_vel = Twist()
	cmd_vel.linear.x = msg.axes[1] / 2
	cmd_vel.angular.z = msg.axes[0]
	#I know that at full range, this would be 0.5 m/s and 1 rad/s?, which is probably impossible
	pub.publish(cmd_vel)

rospy.init_node("dumb_wiimote_nunchuk_teleop_raw")
pub = rospy.Publisher("cmd_vel", Twist)
rospy.Subscriber("wiimote/nunchuk", Joy, nunchuk_cb)
rospy.spin()