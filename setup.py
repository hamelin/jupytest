from setuptools import setup, find_packages
import sys


long_description = """\
You like the super-short try-until-succeed development cycle that comes from
implementing code in a Jupyter notebook? You would also like to perform your
development with a bit of discipline, writing repeatable unit and integration
tests as you go? This Python package is for you.

You can start your notebook by instantiating a test suite, and as you
test-driven-develop your code (or something), you add tests to that suite.
These tests are run as you go. The test suite accumulates your test results
and can produce a report at the end. The package also includes an executable
script that will take your notebook of tests as input, run it all from the
command line, and write a nice result report to the shell -- or some raw test
result data structure, if that's how you fly.

Find out more on `jupytest <https://github.com/hamelin/jupytest>`_'s Github
repository.
"""

setup(
    name="jupytest",
    version="1.0.3",
    packages=find_packages(),
    author="Benoit Hamelin",
    author_email="benoit@benoithamelin.com",
    description="Unit and integration testing in a Jupyter notebook",
    long_description=long_description,
    license="BSD 3-Clause",
    install_requires=["jupyter", "ansicolors", "pygments"],
    url="https://github.com/hamelin/jupytest",
    python_requires=">=3.6"
)
