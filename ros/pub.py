import rospy
import numpy as np
from geometry_msgs.msg import PoseWithCovarianceStamped

if __name__ == '__main__':
    rospy.init_node('publisher_test')

    pose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 10)

    pose_test = PoseWithCovarianceStamped()
    pose_test.header.frame_id = 'map'
    pose_test.pose.pose.position.x = 10.0
    pose_test.pose.pose.position.y = 20.0
    pose_test.pose.pose.orientation.z = np.pi

    while not rospy.is_shutdown():

        pose_pub.publish(pose_test)

        rospy.sleep(0.2)mkdir -p ~/catkin_ws/src
