import pyke
import setuptools

version = pyke.__version__
readme = open("README.md").read()
url = "https://github.com/frissyn/pyke"
description = "Make-like build automation tool for Python projects."

setuptools.setup(
    name="pykefile",

    license="MIT",
    version=version,
    description=description,
    packages=setuptools.find_packages(),
    project_urls={
        "Source Code": url,
        "Pull Requests": url + "/pulls",
        "Issue Tracker": url + "/issues",
    },

    long_description=readme,
    long_description_content_type="text/markdown",

    include_package_data=True,
    python_requires=">=3.8.0",

    entry_points={
        "console_scripts": ["pyke = pyke:runner"]
    },

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
    ],
)