#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from mavros_msgs.msg import OverrideRCIn
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy

"""
Tempo is 105 bpm

c2: roll
c3: up&down
c4: rotate
c5: forwards & backwards
c6: side-to-side


"""
class bestInShow(Node):
    global beat 
    beat = 60/105
    
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

    def roll(self, power, rest):
        msg = OverrideRCIn()
        msg.channels = [OverrideRCIn.CHAN_NOCHANGE] * 18
        msg.channels[1] = power
        self.publisher.publish(msg)
        time.sleep(beat)

    def depth(self, power, rest):
        msg = OverrideRCIn()
        msg.channels = [OverrideRCIn.CHAN_NOCHANGE] * 18
        msg.channels[2] = power
        self.publisher.publish(msg)
        time.sleep(beat)

    def fwd_bkwd(self, power, rest):
        msg = OverrideRCIn()
        msg.channels = [OverrideRCIn.CHAN_NOCHANGE] * 18
        msg.channels[4] = power
        self.publisher.publish(msg)
        time.sleep(beat)

    def horizontal(self, power, rest):
        msg = OverrideRCIn()
        msg.channels = [OverrideRCIn.CHAN_NOCHANGE] * 18
        msg.channels[3] = power
        self.publisher.publish(msg)
        time.sleep(beat)

    def rotation(self, power, rest):
        msg = OverrideRCIn()
        msg.channels = [OverrideRCIn.CHAN_NOCHANGE] * 18
        msg.channels[5] = power
        self.publisher.publish(msg)
        time.sleep(beat)

    def at_rest(self):
        msg = OverrideRCIn()
        msg.channels = [1500] * 18
        self.publisher.publish(msg)

    
       

def hcb(self):
    hot(self)
    cross(self)
    buns(self)
    time.sleep(beat)

def pennies(self):
    #Up & down
    pass

def children(self):
    daughters(self)
    sons(self)

def rave(self):
    #barrel rolls
    """
    down for three, roll for 5 (or the rest of the time)
    """
    self.roll(1700)
    pass

def hot(self):
    #left 90
    self.rotation(1700)
    pass

def cross(self):
    #right 180
    pass

def buns(self):
    #left 360
    pass

def daughters(self):
    #45 back and forth (like a head shake)
    pass

def sons(self):
    #fwd & bkwd
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


    






