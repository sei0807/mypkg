# SPDX-FileCopyrightText: 2025 Seiya Ohata
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.pub = self.create_subscription(Int16, 'count', self.cb, 10)
        self.pos = 0

    def cb(self, msg):
        self.pos += msg.data
        self.get_logger().info(
            "Velocity: %d, Current Position: %d" %
            (msg.data, self.pos))


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
