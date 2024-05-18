.PHONY: run clean

run:
	python3 Problema2.py < input-3.dat > output-3.dat

clean:
	rm -rf __pycache__ *.pyc
