test:
	nosetests --with-coverage --cover-package=faker_schema --cover-erase -v --cover-html

flake8:
	flake8 --max-line-length 99 faker_schema/ tests/