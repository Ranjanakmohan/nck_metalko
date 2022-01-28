from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nck_metalko/__init__.py
from nck_metalko import __version__ as version

setup(
	name="nck_metalko",
	version=version,
	description="Nck Metalko",
	author="jan",
	author_email="janlloydangeles@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
