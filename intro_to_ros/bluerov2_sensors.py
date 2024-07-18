#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState, Imu
from rcply.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
import numpy as np

class blueROV2Sensors(Node):
  
  battery_msg = None
  imu_msg = None

  def __init__(self):
    '''
  Initializing node 
  creating essential vars and timer 
  '''
    #Subscription vars format
    #self.<VAR NAME> = self.create_subscription(<??>, "<topic>", self.<function calling raw data>, qosProfile)

    super().__init__("tutorial_subscriber")

    #Reads batteryState data
    self.battery_sub = self.create_subscription(
      BatteryState,
      "/mavros/battery",
      self.callback,
      qosProfile
    )

    #Reads IMU data
    self.imu_sub = self.create_subscription(
      Imu,
      "/mavros/imu/data",
      self.callback,
      qosProfile
    )

    #Reads static pressure
    #!!!NOT CORRECT SENSOR!!!
    self.static_pressure = self.create_subscription(
      FluidPressure,
      "mavros/imu/static_pressure",
      self.static_pressure_cb,
      qosProfile
    )

    #reads differential pressure (AKA ??)
    #not ideal to use bc small errors grow exponentially
    self.differential_pressure = self.create_subscription(
      FluidPressure,
      "/mavros/imu/diff_pressure",
      self.differential_pressure_cb,
      qosProfile
    )

#checks for safe voltage levels every 5 seconds
    self.publisher_timer = self.create_timer(
      5.0, check_voltage(self, battery_msg, battery_subscriber, imu_msg, imu_subscriber)
    )
    
    #Establishing variables exist (good practice)
    self.battery_subscriber
    self.imu_subscriber
    self.get_logger().info("starting subscriber node")



  def check_voltage(self, battery_msg, battery_subscriber, imu_msg, imu_subscriber, msg):
    self.battery_msg = self.battery_subscriber
    self.imu_msg = self.imu_subscriber

    print(f"Battery voltage: {self.battery_msg}")

    if self.battery_msg < 12:
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