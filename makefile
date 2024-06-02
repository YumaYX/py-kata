default:
	for i in $$(ls -1 src/*.py); do python3 $$i; done

test:
	python3 -m unittest discover tests/ "test_*.py"

clean:
	rm -rf ./*.txt ./*.json

update: test clean
	git status
	sleep 5
	git add .
	git commit -am 'update'
	git push