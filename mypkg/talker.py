# Copyright 2025 Seiya Ohata
# Licensed under the 3-Clause BSD License

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Int16, 'count', 10)
        self.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = random.randint(-1, 1)
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
