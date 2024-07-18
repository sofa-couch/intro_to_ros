#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
import time
import numpy as np

class SensorSubscriber(Node):

  battery_type = None
  imu_type = None

  def __init__(self):
    super().__init__("tutorial_subscriber")

    self.battery_subscriber = self.create_subscription(
      BatteryState,
      "/marvos/battery",
      self.callback,
      10
    )

    self.imu_subscriber = self.create_subscription(
      Imu,
      "/marvos/imu/data",
      self.callback,
      10
    )

    self.publisher_timer = self.create_timer(
      5.0, check_voltage(self, battery_type, battery_subscriber, imu_type, imu_subscriber)
    )
    
    self.battery_subscriber
    self.imu_subscriber
    self.get_logger().info("starting subscriber node")



  def check_voltage(self, battery_type, battery_subscriber, imu_type, imu_subscriber, msg):
    self.battery_type = self.battery_subscriber
    self.imu_type = self.imu_subscriber

    if self.battery_type < 12:
      self.get_logger("Battery has fallen below a safe voltage")



def main(args=None):
    rclpy.init(args=args)
    node = TutorialSubscriber()

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