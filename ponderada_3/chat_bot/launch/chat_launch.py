from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='chat_bot',
            executable='test-chatbot',
            output='screen',
            name='chat_bot'
        )
    ])
