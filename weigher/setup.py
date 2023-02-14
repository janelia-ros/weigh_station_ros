from setuptools import setup

package_name = 'weigher'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Peter Polidoro',
    maintainer_email='peter@polidoro.io',
    description='ROS 2 weigh scale interface. ',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weigher_node = weigher.weigher_node:main'
        ],
    },
    data_files=[
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ]
)
