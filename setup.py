from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in snd_tinymce_editor/__init__.py
from snd_tinymce_editor import __version__ as version

setup(
	name="snd_tinymce_editor",
	version=version,
	description="Sanad tinymce Editor",
	author="Sanad",
	author_email="alhakeem.prof@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
