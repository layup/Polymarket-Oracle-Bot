run: 
	python3 setup.py 

clean: 
	rm -rf __pychace__

setup: requirements.txt
	pip install -r requirements.txt

