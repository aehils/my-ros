#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class ControllerClientNode(Node):

    def __init__(self):
        super().__init__("control_turtle_client")
        self.get_logger().info("Client Node started.")
        self.pose_sub_ = self.create_subscription(
                Pose, "/turtle1/pose", self.callback_pose_sub, 10)
        self.command_pub = self.create_publisher(
                Twist, "/turtle1/cmd_vel", 10)

    def callback_pose_sub(self, pose: Pose):
        cmd = Twist()
        if pose.x < 2.0 or pose.x > 9.0 or \
                pose.y < 2.0 or pose.y > 9.0:
                    cmd.linear.x = 1.0
                    cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.command_pub.publish(cmd)



def main(args=None):

    rclpy.init(args=args)
    node = ControllerClientNode()
    rclpy.spin(node)
    rclpy.shutdown()
