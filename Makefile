all:
	python setup.py bdist_wheel
	git add *
<<<<<<< HEAD
	@echo "Enter a commit message"
	@read message;\
=======
	@read -p "Enter a commit message:" message;\
>>>>>>> df1e8e7e24444aa50c035e63fb4529ea539706ee
	git commit -m $$message;
	git push
init:
	pip install -r requirements.txt

test:
	nosetests -v -s
