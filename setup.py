"""Setup configuration for the cow project."""

from setuptools import setup, find_packages

setup(
    name="cow",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
