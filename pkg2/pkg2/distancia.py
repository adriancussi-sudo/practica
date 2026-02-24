import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MySubscriber(Node):

    def __init__(self):
        super().__init__('mi_suscriptor')
        self.subscription = self.create_subscription(
            String,
            'adrianc',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        numero = int(msg.data)
        if numero <= 5:
            self.get_logger().info("Alert")
        else:
            self.get_logger().info("OK")


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MySubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
