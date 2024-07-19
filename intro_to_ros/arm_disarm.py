#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from mavros_msg.srv import CommandBool
from rcply.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
import numpy as np

class armDisarm(Node):
    def __init__(self):
        super().__init__("ARM")

        self.client = self.create_client(CommandBool, 'mavros/cmd/arming')
        
        while not self.client.wait_for_service(timeout_sec = 1):
            self.get_logger().info('Service unavailable.  Retrying.')
        self.request = CommandBook.Request()

    def arm_request(self, msg):
        self.msg.value = value
        self.future = self.client.call_async(self, msg)
        return self.next


def main(args=None):
    rclpy.init(args=args)
    node = TutorialSubscriber()

    try:
        next = node.arm_request(bool(True))
        rcply.cont_until_done(node, next)
        response = next.result
        node.get_logger().info('Robot armed')
        rclpy.spin(node)
    except KeyboardInterrupt:
        next = node.arm_request(bool(False))
        rcply.cont_until_done(node = node, next = next)
        response = future.result()
        node.get_logger().info('Robot disarmed')
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__=="__main__":
    main()