#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from mavros_msg.srv import CommandBool
from rcply.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
import numpy as np

#joystick controls

class thrusterControl(Node):
    def __init__(self):
        super().__init__("X", "Y")



