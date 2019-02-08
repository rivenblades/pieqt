all:
	python setup.py bdist_wheel
	git add *
	@echo "Enter a commit message"
	@read message;\
	git commit -m $$message;
	git push
init:
	pip install -r requirements.txt

test:
	nosetests -v -s
