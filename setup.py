"""Setup configuration for the cow project."""

from setuptools import setup, find_packages

setup(
    name="cow",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
