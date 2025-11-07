from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="moo",
    packages=find_namespace_packages(include=["moo", "moo.*"]),
    python_requires='>=3.8',
    install_requires=['numpy>=1.23.5']
)
