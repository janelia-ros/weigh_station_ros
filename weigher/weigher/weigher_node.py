import rclpy
from rclpy.node import Node

from weigher_interfaces.msg import Weight

from loadstar_sensors_interface import LoadstarSensorsInterface
import asyncio



class Weigher(Node):

    def __init__(self):
        super().__init__('weigher')
        self.get_logger().info('Initializing Weigher Node')
        self.declare_parameter('debug', False)
        debug = self.get_parameter('debug').get_parameter_value().bool_value
        self.declare_parameter('serial_port', '/dev/ttyUSB0')
        self._publisher = self.create_publisher(Weight, 'weight', 10)
        self._dev = LoadstarSensorsInterface(debug=debug)

    async def start_getting_sensor_values(self):
        serial_port = self.get_parameter('serial_port').get_parameter_value().string_value
        self.get_logger().info(f'start_getting_sensor_values on serial port: {serial_port}')
        await self._dev.open_high_speed_serial_connection(port=serial_port)
        self._dev.set_sensor_value_units('gram')
        self._dev.set_units_format('.1f')
        await self._dev.tare()
        self._dev.start_getting_sensor_values(self.sensor_value_callback)

    async def stop_getting_sensor_values(self):
        self.get_logger().info('stop_getting_sensor_values')
        await self._dev.stop_getting_sensor_values()

    async def sensor_value_callback(self, sensor_value):
        msg = Weight()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.weight = sensor_value.magnitude
        self._publisher.publish(msg)
        await asyncio.sleep(0)


async def async_main():
    weigher = Weigher()

    await weigher.start_getting_sensor_values()

    while rclpy.ok():
        rclpy.spin_once(weigher, timeout_sec=0)
        await asyncio.sleep(1e-4)

    await weigher.stop_getting_sensor_values()

    weigher.destroy_node()

def main(args=None):
    rclpy.init(args=args)

    asyncio.run(async_main())

    rclpy.shutdown()


if __name__ == '__main__':
    main()
