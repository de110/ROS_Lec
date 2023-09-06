import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class MyServiceClient(Node):
    def __init__(self):
        super().__init__('client_node')
        self.client = self.create_client(AddTwoInts, 'add_two_ints_jas')   # service name unique하게 설정 (이름 이니셜)
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service waiting...')
        self.req = AddTwoInts.Request()

    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    service_client = MyServiceClient()
    service_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(service_client)
        if service_client.future.done():
            try:
                response = service_client.future.result()
            except Exception as e:
                service_client.get_logger().info('service call failed %r' % (e,))
            else:
                service_client.get_logger().info('Result of add_two_int_jas: for %d + %d = %d' % (service_client.req.a, service_client.req.b, response.sum))
            break
    service_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


