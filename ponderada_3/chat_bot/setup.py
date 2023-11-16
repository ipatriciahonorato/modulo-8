from setuptools import find_packages, setup

package_name = 'chat_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/chat_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='patricia',
    maintainer_email='patricia.moreira@sou.inteli.edu.br',
    description='Descrição do Pacote Chat Bot',
    license='Licença (ex: MIT)',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test-chatbot = chat_bot.test_chatbot:main',        
        ],
    },
)