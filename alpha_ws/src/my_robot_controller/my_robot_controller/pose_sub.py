#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subsciber")
        self.subsriber_ = self.create_subscription(
                Pose, "turtle1/pose", self.pose_sub_callback, 10)

    def pose_sub_callback(self, msg:Pose):
        self.get_logger().info("x: " + str(msg.x) + ", y: " + str(msg.y))

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

