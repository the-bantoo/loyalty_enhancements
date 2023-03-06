from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in loyalty_enhancements/__init__.py
from loyalty_enhancements import __version__ as version

setup(
	name="loyalty_enhancements",
	version=version,
	description="ERPNext Loyalty Enhancements",
	author="Bantoo",
	author_email="devs@thebantoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
