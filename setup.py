from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in payment_maintenance/__init__.py
from payment_maintenance import __version__ as version

setup(
	name="payment_maintenance",
	version=version,
	description="Payment Maintenance application is a custom app for the customers and the suppliers to the person who sells goods.And [Dmaintains the payment system.",
	author="Srijena_Nithish",
	author_email="srijenanithish@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
