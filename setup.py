from setuptools import setup
from setuptools import find_packages
import codecs, os

def readme():
    with open("README.md") as file:
        return file.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
setup(
    name="pytail-r3ap3rpy",
    version = get_version('pytail/__init__.py'),
    long_description = readme(),
    long_description_content_type = "text/markdown",
    author = "Szabó Dániel Ernő",
    author_email = "r3ap3rpy@gmail.com",
    url = "",
    license = "MIT",
    packages=find_packages(),
    scripts=["bin/pytail"],
    classifiers= [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
