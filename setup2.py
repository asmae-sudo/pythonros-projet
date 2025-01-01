from setuptools import setup
package_name = 'security_monitor'
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='VotreNom',
    maintainer_email='votre-email@example.com',
    description='Surveillance de la sécurité et détection des anomalies',
    license='Licence',
    entry_points={
        'console_scripts': [
            'security_monitor = security_monitor.security_monitor:main',
            'anomaly_alarm = security_monitor.anomaly_alarm:main',
        ],
    },
)
