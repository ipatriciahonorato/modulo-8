from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='chat_bot',
            namespace='chat_bot',
            executable='test-chatbot',
            name='chat_bot'
        )
    ])
