test:
	python3 -m unittest discover tests/ "test_*.py"

clean:
	rm -rf ./*.txt

update: test clean
	git status
	sleep 5
	git add .
	git commit -am 'update'
	git push
