#! /bin/bash

printf "Cleaning previous Building and Distributions"
rm -r dist
rm -r build
rm -r *.egg-info

printf "Preparing  Source and Binary Distributions"
python3 setup.py sdist bdist_wheel

printf "Uploading to Pypi"
twine upload dist/*
