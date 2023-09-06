import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class subs_tof(Node): # Node 클래스
    
    def __init__(self):
        super().__init__('subscriber_tof') # ‘subscriber_tof’ 이름의 클래스 생성자 호출
        self.subscription=self.create_subscription(Range,'tof',self.listener_callback,10)
# subscriber 설정, (토픽 메시지 타입, 토픽 이름, 호출 함수, QoS)
        self.range=0

    def listener_callback(self,msg):
        self.range=msg.range
        self.get_logger().info('sensor is seeing obstacle in distance: %f'%self.range)

def main(args=None):
    rclpy.init(args=args) # 초기화

    minimal_subscriber = subs_tof() # subs_tof 클래스 생성

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()    
