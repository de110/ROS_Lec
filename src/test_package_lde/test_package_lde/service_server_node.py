import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts
from my_interfaces_lde.srv import AddThreeInts

class MyServiceServer(Node):
    def __init__(self):
        super().__init__('server_node')
        self.srv = self.create_service(AddThreeInts, 'add_two_ints_jas', self.add_two_ints_callback)    # service name unique하게 설정 (이름 이니셜)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info('Incoming request.. a: %d b: %d c: %d' % (request.a, request.b, request.c))
        return response

def main(args=None):
    rclpy.init(args=args)
    node = MyServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()








