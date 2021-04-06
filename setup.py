from sys import version_info
from setuptools import setup
from os import name as os_name


if os_name != "posix":
    raise OSError(f"Unsported OS: {os_name}")

if version_info < (3, 5):
    raise RuntimeError("pythonfetch requires Python 3.5 or later")

with open("README.md") as f:
    long_description = f.read()


setup(
    name="binali",
    packages=["binali"],
    version="1.0.0",
    description="/bin/ali is a script which echo well-known quotes from binali.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beucismis-archive/binali",
    project_urls={
        "Forked from": "https://github.com/kozdincer/binali",
    },
    author="Kaan Özdinçer",
    author_email="kaanozdincer@gmail.com",
    license="WTFPL",
    classifiers=[
        "Environment :: Console",
        "Natural Language :: Turkish",
        "Operating System :: POSIX :: Linux",
    ],
    platforms=["Linux"],
    python_requires=">=3.5",
    keywords=["bin ali binali"],
    entry_points={
        "console_scripts": [
            "binali = binali:main",
        ],
    },
)
