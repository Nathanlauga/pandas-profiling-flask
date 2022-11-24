from setuptools import setup, find_packages
import os

path = os.path.dirname(os.path.abspath(__file__))
with open(path + "/README.md", "r") as fh:
    long_description = fh.read()
fh.close()

setup(
    name="pandas-profiling-webapp",
    version="1.0.0",
    license="MIT",
    author="Nathan LAUGA",
    author_email="nathan.lauga@protonmail.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["click", "flask", "pandas-profiling", "gunicorn"],
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pandas-profiling-webapp = pandas_profiling_webapp.__main__:main"
        ]
    },
)
