from setuptools import setup
import os

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, 'wip', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='wip',
    version=version['__version__'],
    packages=['wip'],
    install_requires=['py_trees'],
    entry_points={
        'console_scripts': [
            'run-robot=wip:main',
            'run-robot-docker=wip.docker:main_docker',
        ],
    },
)
