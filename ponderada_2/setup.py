import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ponderada_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='patricia',
    maintainer_email='patricia@example.com',  # Substitua pelo seu e-mail real
    description='Descrição do pacote ponderada_2',  # Descrição do seu pacote
    license='Apache-2.0',  # Licença do seu pacote
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pose_inicial = ponderada_2.nav2_test:main',
            'nav2_go_to_pose = ponderada_2.nav2_go_to_pose:main',
            'nav_waypoints = ponderada_2.nav_waypoints:main',
        ],
    },
)

