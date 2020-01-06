from setuptools import setup, find_packages
from subprocess import run, PIPE
import sys


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f.readlines()]

cp = run(["git", "describe", "--always"], stdout=PIPE, encoding="utf-8")
if cp.returncode != 0:
    print("Problem while gathering software version. Abort.")
    sys.exit(cp.returncode)
version = cp.stdout.strip()
print("Version:", version)

setup(
    name="jupytest",
    version=version,
    packages=find_packages(),
    author="Benoit Hamelin",
    author_email="benoit@benoithamelin.com",
    description="Unit and integration testing in a Jupyter notebook",
    long_description=long_description,
    install_requires=requirements,
    url="https://github.com/hamelin/jupytest",
    python_requires=">=3.6"
)
