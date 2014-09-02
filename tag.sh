#!/bin/bash 
echo current version:$(python setup.py --version)
read -p "new version:" new_version
git tag -s ${new_version} -m "tagging version ${new_version}"
python setup.py build sdist bdist_egg upload


