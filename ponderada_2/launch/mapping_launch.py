from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Inicializa o TurtleBot 3 no Webots
        Node(
            package='webots_ros2_turtlebot',
            executable='robot_launch.py',
            name='webots_robot',
            output='screen'
        ),

        # Lança o processo de mapeamento e navegação com Nav2
        Node(
            package='nav2_bringup',
            executable='tb3_simulation_launch.py',
            name='nav2_bringup',
            output='screen',
            arguments=['slam:=True']
        )
    ])
