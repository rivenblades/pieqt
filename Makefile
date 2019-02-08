all:
	python setup.py bdist_wheel
	git add *
	@read -p "Enter a commit message:" message;\
	git commit -m $$message;
	git push
init:
	pip install -r requirements.txt

test:
	nosetests -v -s
