#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState, Imu
from rcply.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
import numpy as np

class blueROV2Sensors(Node):
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
      self.battery_cb,
      qosProfile
    )
    self.battery_sub

    #Reads IMU data
    self.imu_sub = self.create_subscription(
      Imu,
      "/mavros/imu/data",
      self.imu_cb,
      qosProfile
    )
    self.imu_sub

    #Reads static pressure
    #!!!NOT CORRECT SENSOR!!!
    self.static_pressure = self.create_subscription(
      FluidPressure,
      "mavros/imu/static_pressure",
      self.static_pressure_cb,
      qosProfile
    )
    self.static_pressure

    #reads differential pressure (AKA ??)
    #not ideal to use bc small errors grow exponentially
    #also wrong sensor
    self.differential_pressure = self.create_subscription(
      FluidPressure,
      "/mavros/imu/diff_pressure",
      self.differential_pressure_cb,
      qosProfile
    )
    self.differential_pressure

    #calls timer
    self.timer = self.create_timer(5, self.check_voltage)

    self.get_logger().info("starting subscriber node")




  def check_voltage(self):
    '''
    checks to make sure battery is at a safe voltage
    '''
    voltage = self.battery_sub.voltage
    print(f"Battery voltage: {voltage}")
    if self.battery_msg < 12:
      self.get_logger("Battery has fallen below a safe voltage")


  def imu_cb(self, msg):
    self.imu_msg = msg
    self.get_logger().info(f"IMU accel: {msg.linear_acceleration}")

  def static_pressure_cb(self, mag):
    atm = 101325
    gravity = 9.81
    self.s_pressure_msg = imu_msg
    self.get_logger().info(f"Static pressure: {msg.fluid_pressure}")
    self.get_logger().info(f"Depth: {(msg-atm)/gravity/1000}")

  def differential_pressure_cb(self, msg):
    self.diff_pressure_msg = msg
    self.get_logger(). info(f"Diff Pressure: {msg.fluid_pressure}")



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