from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elishaokara',
    maintainer_email='elishaokara@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "alpha_node= my_robot_controller.node1:main",
            "circle_node= my_robot_controller.drawcircle:main",
            "pose_subscribe= my_robot_controller.pose_sub:main",
            "control_turtle= my_robot_controller.robotcontroller:main"
        ],
    },
)
