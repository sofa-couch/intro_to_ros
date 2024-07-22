#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from mavros_msgs.msg import OverrideRCIn
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy


class bestInShow(Node):
    def __init__(self):
        super().__init__("best_in_show")
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.SYSTEM_DEFAULT,
            depth=10
        )
        self.publisher = self.create_publisher(OverrideRCIn, "/mavros/rc/override", qos_profile
        )
        self.get_logger().info("Publishing")
       

    def hcb(self):
        hot(self)
        cross(self)
        buns(self)

    def pennies(self):
        pass

    def children(self):
        daughters(self)
        sons(self)

    def rave(self):
        pass

    def hot(self):
        pass

    def cross(self):
        pass

    def buns(self):
        pass

    def daughters(self):
        pass

    def sons(self):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = bestInShow()

    try:
        time.sleep(9.3)
        for i in range(2):
            rclpy.hcb(node)
        time.sleep(14.4)
        rclpy.pennies(node)
        time.sleep(16.8)
        rclpy.hcb(node)
        time.sleep(19.7)
        rclpy.children(node)
        time.sleep(23.0)
        rclpy.rave(node)
        time.sleep(30.3)
        rclpy.pennies(node)
        time.sleep(32.6)
        rclpy.hot(node)
        time.sleep(33.2)
        rclpy.cross(node)
        time.sleep(33.8)
        rclpy.rave(node)
        time.sleep(55.5)
        rclpy.sons(node)
        time.sleep(56.4)
        rclpy.pennies(node)
        time.sleep(59.3)
        rclpy.hcb(node)


    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__=="__main__":
    main()


    






