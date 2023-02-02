import rclpy
from rclpy.node import Node

from weigher_interfaces.msg import Weight


class Weigher(Node):

    def __init__(self):
        super().__init__('weigher')
        self.publisher_ = self.create_publisher(Weight, 'weight', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Weight()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.weight = self.i + 0.1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.weight)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    weigher = Weigher()

    rclpy.spin(weigher)

    weigher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
