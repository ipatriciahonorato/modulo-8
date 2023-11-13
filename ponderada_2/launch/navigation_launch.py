from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Caminho para o pacote 'ponderada_2'
    pkg_share = FindPackageShare(package='ponderada_2')

    # Caminho para o arquivo do mapa dentro do pacote
    map_file_path = PathJoinSubstitution([pkg_share, 'maps', 'mapafinal.yaml'])

    # Argumento para especificar o arquivo do mapa
    map_file_arg = DeclareLaunchArgument(
        'map_file', default_value=map_file_path,
        description='Caminho para o arquivo do mapa'
    )

    return LaunchDescription([
        map_file_arg,

        # Inicializa o TurtleBot 3 no Webots
        Node(
            package='webots_ros2_turtlebot',
            executable='robot_launch.py',
            name='webots_robot',
            output='screen'
        ),

        # Lança o processo de navegação com Nav2
        Node(
            package='nav2_bringup',
            executable='tb3_simulation_launch.py',
            name='nav2_bringup',
            output='screen',
            arguments=['map:=' + LaunchConfiguration('map_file')]
        ),

        # Executa o script de definição da pose inicial
        ExecuteProcess(
            cmd=['python3', PathJoinSubstitution([pkg_share, 'nav2_test.py'])],
            output='screen'
        ),

        # Executa o script para enviar o robô a uma pose
        ExecuteProcess(
            cmd=['python3', PathJoinSubstitution([pkg_share, 'nav2_go_to_pose.py'])],
            output='screen'
        ),

        # Executa o script de navegação por waypoints
        ExecuteProcess(
            cmd=['python3', PathJoinSubstitution([pkg_share, 'nav_waypoints.py'])],
            output='screen'
        )
    ])
