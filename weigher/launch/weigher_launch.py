from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution


def generate_launch_description():
    serial_port_arg = DeclareLaunchArgument(
      'serial_port', default_value=TextSubstitution(text='/dev/ttyUSB0')
    )
    threshold_arg = DeclareLaunchArgument(
      'threshold', default_value=TextSubstitution(text='100')
    )

    return LaunchDescription([
        serial_port_arg,
        Node(
            package='weigher',
            executable='weigher_node',
            name='weigher',
            parameters=[{
            'serial_port': LaunchConfiguration('serial_port'),
            'threshold': LaunchConfiguration('threshold'),
         }]
        )
    ])
