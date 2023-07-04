from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Generates a grouped frequency distribution table from a dataset.'
LONG_DESCRIPTION = 'A package that allows you to generate a grouped frequency distribution table and calculates measures of central tendency and dispersion from a dataset.'

# Setting up
setup(
    name="grouped_distribution_table",
    version=VERSION,
    author="Ismael Sandoval, Mauricio Ponce",
    author_email="ismael.sandoval.aguilar@gmail.com, maupon2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'distribution', 'statistics', 'table', 'data', 'grouped'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)