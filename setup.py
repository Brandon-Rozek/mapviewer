from setuptools import setup, find_packages
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

# Recursively get the templates and static files
data_files = []
data_directories = glob('mapviewer/templates/**/', recursive=True) + \
                   glob('mapviewer/static/**/', recursive=True)

for directory in data_directories:
    files = filter(lambda x: x not in data_directories, glob(directory + "*"))
    data_files.append((directory, files))

setup(
    name="mapviewer",
    description="Map Tile Server Viewer",
    version="1.0",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    data_files=data_files,
    scripts=['viewtiles'],
    install_requires=['Flask~=1.1.2', 'gevent~=21.1.2'],
    python_requires='>=3.7'
)
