#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Controller node is started.")

        self.pose_sub = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.vel_pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if (pose.x > 9.0) or (pose.x < 2.0):
            cmd.linear.x = 1.2
            cmd.angular.z = 1.0
            self.vel_pub.publish(cmd)
        else:
            cmd.linear.x = 4.0
            cmd.angular.z = 0.0
            self.vel_pub.publish(cmd)


def main(args=None):
    rclpy.init()
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
