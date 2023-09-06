import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class subs_tof(Node):
    
    def __init__(self):
        super().__init__('subscriber_tof')
        self.subscription = self.create_subscription(Range,'tof',self.listener_callback,10)
        self.range=0

    def listener_callback(self,msg):
        self.range=msg.range
        self.get_logger().info('sensor is seeing obstacle in distance: %f'%self.range)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = subs_tof()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()    
