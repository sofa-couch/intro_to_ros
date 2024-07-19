#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from mavros_msgs.msg import OverrideRCIn
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy

class Movement(Node):
    def __init__(self):
        super().__init__("movement")
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.SYSTEM_DEFAULT,
            depth=10
        )
        self.publisher = self.create_publisher(OverrideRCIn, "/mavros/rc/override", qos_profile
        )
        self.get_logger().info("Publishing")

        self.publisher_timer = self.create_timer( 5.0, self.run_node )

    
    def run_node(self):
        channels = [1700,1700,1700,1700,1700,1700,
                    OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,
                    OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,
                    OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,
                    OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,OverrideRCIn.CHAN_NOCHANGE,]
        self.publisher.publish(channels)
        self.get_logger().info(f"Inputs: {channels[0]}, {channels[1]}")

def main(args=None):
    rclpy.init(args=args)
    node = Movement()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__=="__main__":
    main()