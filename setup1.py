from setuptools import setup

package_name = 'password_manager'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    data_files=[
        ('lib/python3.8/site-packages', ['src/password_manager/password_creator.py', 'src/password_manager/password_cli.py']),
    ],
    entry_points={
        'console_scripts': [
            'password_creator = password_manager.password_creator:main',
            'password_cli = password_manager.password_cli:main',
        ],
    },
)

