import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class MySubscriber(Node):    # Node 클래스 상속
    def __init__(self):
        super().__init__('my_subscriber') # Node 클래스 생성자 호출, 노드 이름 'my_subscriber'
        self.sample_subscriber = self.create_subscription(    
            String,    # topic_A 와 같은 메시지 타입
            'topic_A_jas',
            self.subscribe_topic_message,
            10
        ) # 서브스크라이버 설정
        
    def subscribe_topic_message(self, msg):
        self.get_logger().info('I heard: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    my_subscriber = MySubscriber()
    rclpy.spin(my_subscriber)
    rclpy.shutdown()

if __name__ == '__main__' :
    main()

    