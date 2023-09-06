from setuptools import setup

package_name = 'test_package_lde'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='skyyk',
    maintainer_email='201720092@sangmyung.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher_node = test_package_jas.simple_publisher_node:main',
            'simple_subscriber_node = test_package_jas.simple_subscriber_node:main',
            'temperature_sensor = test_package_jas.temperature_sensor:main',
            'temperature_alert = test_package_jas.temperature_alert:main',
            'service_server_node = test_package_jas.service_server_node:main',
            'service_client_node = test_package_jas.service_client_node:main',
            'fibonacci_action_server = test_package_jas.fibonacci_action_server:main'
        ],
    },
)
