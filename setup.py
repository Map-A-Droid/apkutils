import os.path

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="apkutils-mad",

    version='0.0.1',

    description=("Utils for parsing apk."),
    long_description=read('README.rst'),

    url="https://github.com/map-a-droid/apkutils",

    author="map-a-droid dev team",

    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],

    keywords="apk dex axml",

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        "anytree",
        "cigam",
        "pyelftools",
        "pyopenssl",
        "xmltodict",
        "beautifulsoup4",
    ],
)
