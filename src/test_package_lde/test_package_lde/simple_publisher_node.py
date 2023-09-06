import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String

class MyPublisher(Node):  # Node 클래스 상속
    def __init__(self) :
        super().__init__('my_publisher')  # Node 클래스 생성자 호출, 노드 이름 'my_publisher'
        self.sample_publisher = self.create_publisher(String, 'topic_A_jas', 10)   # sample_publisher 라는 퍼블리셔 설정 (토픽 메시지 타입, 토픽 이름, QoS설정)
        self.timer = self.create_timer(1, self.timer_callback)  # 1초마다 timer_callback 함수 실행
        self.i = 0 

    def timer_callback(self) :
        msg = String()    # publish할 메시지 타입은 String
        msg.data = 'Hello ROS2: %d' % self.i   # msg.data 에 publish할 문자열(string) 입력    
        self.i += 1
        self.sample_publisher.publish(msg)  # 퍼블리셔에 메시지 publish
        self.get_logger().info('Publishing: "%s"' % msg.data)   # (optional) 터미널에 출력

def main(args=None):
    rclpy.init(args=args)      # 초기화
    print('Hi from test_package.')      # (optional) 터미널에 출력
    node = MyPublisher()    # MyPublisher 클래스 생성
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
