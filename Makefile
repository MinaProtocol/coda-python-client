install:
	pip3 install -e .

dist: 
	python3 setup.py sdist bdist_wheel

dist-upload:
	twine upload --username $PYPI_USER --password $PYPI_PASSWORD dist/*