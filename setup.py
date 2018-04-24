import os
from setuptools import setup

data_files = []
for root, dirs, files in os.walk("lib/domains"):
    data_files.append((os.path.join("swot_lib", root), [os.path.join(root, f) for f in files]))

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="swot",
    version="1.0.1",
    description=("Swot is a community-driven or crowdsourced library for verifying "
    "that domain names and email addresses are tied to a legitimate university of college."),
    long_description=long_description,
    keywords="swot email academic university college verification identification",
    author="Zakaria Elkatani",
    author_email="zelkatani@gmail.com",
    license="MIT",
    url="http://github.com/ze/swot",
    data_files=data_files,
    py_modules=["swot"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)