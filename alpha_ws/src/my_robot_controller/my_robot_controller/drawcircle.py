#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("do_circle")
        self.get_logger().info("Drawing a circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.sendVel)


    def sendVel(self):
        msg = Twist()
        msg.linear.x = 0.75
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


