all:
	python setup.py bdist_wheel
	git add *
	git commit -m "Update"
	git push
	twine upload dist/*
init:
	pip install -r requirements.txt

test:
	nosetests -v -s
