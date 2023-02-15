import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def pose_callback(msg_pose):
    global subscribed_pose
    subscribed_pose = msg_pose

if __name__ == '__main__':
    rospy.init_node('subscriber_test')

    pose_sub = rospy.Subscriber('/initialpose', PoseWithCovarianceStamped, pose_callback)

    subscribed_pose = PoseWithCovarianceStamped()

    while not rospy.is_shutdown():

        rospy.loginfo(subscribed_pose)

        rospy.sleep(0.2)
