import rclpy
from rclpy.node import Node

from weigher_interfaces.msg import Weight

from loadstar_sensors_interface import LoadstarSensorsInterface
import asyncio



class Weigher(Node):

    def __init__(self):
        super().__init__('weigher')
        self._publisher = self.create_publisher(Weight, 'weight', 10)
        self._dev = LoadstarSensorsInterface()

    async def start(self):
        await self._dev.open_high_speed_serial_connection(port='/dev/ttyUSB0')
        self._dev.set_sensor_value_units('gram')
        self._dev.set_units_format('.1f')
        await self._dev.tare()
        self._dev.start_getting_sensor_values(self.sensor_value_callback)

    async def stop(self):
        await self._dev.stop_getting_sensor_values()
        self.destroy_node()

    async def sensor_value_callback(self, sensor_value):
        msg = Weight()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.weight = sensor_value.magnitude
        self._publisher.publish(msg)
        await asyncio.sleep(0)


async def async_main():
    weigher = Weigher()
    await weigher.start()

    while rclpy.ok():
        rclpy.spin_once(weigher, timeout_sec=0)
        await asyncio.sleep(1e-4)

    await weigher.stop()

def main(args=None):
    rclpy.init(args=args)

    asyncio.run(async_main())

    rclpy.shutdown()


if __name__ == '__main__':
    main()
