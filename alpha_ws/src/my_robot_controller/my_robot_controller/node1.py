#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class myNode(Node):

    def __init__(self):
        super().__init__("alpha_node")
        self.counter_ = 1
        self.get_logger().info("Alpha node started")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Count at " + str(self.counter_))
        self.counter_ += 1

def main(args=None):

    rclpy.init()
    node = myNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

