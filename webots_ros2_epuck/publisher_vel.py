import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class publisher_vel(Node): # Node 클래스

    def __init__(self):
        super().__init__('cmd_vel_publisher')
# 이름이 cmd_vel_publisher인 node 클래스 생성자 호출
        self.publisher_ =self.create_publisher(Twist, 'cmd_vel', 10)
# publisher 설정(토픽 메시지 타입, 토픽 이름, QoS)
        timer_period =0.5
        self.timer =self.create_timer(timer_period, self.timer_callback)
# 0.5초 마다 timer_callback 함수 실행

    def timer_callback(self):
        msg = Twist()
# Twist 타입의 메시지 설정
        msg.linear.x =0.1
        msg.angular.z =0.5
# 로봇 진행 속도 지정
        self.publisher_.publish(msg)
# 메시지 publish

def main(args=None):
    rclpy.init(args=args) # 초기화

    publisher_obj = publisher_vel() # publisher_vel 클래스 생성

    rclpy.spin(publisher_obj)

    publisher_obj.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
