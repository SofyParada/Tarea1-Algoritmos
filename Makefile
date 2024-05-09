.PHONY: run clean

run:
	python3 Problema1.py < input-1.dat > output-1.dat
  python3 Problema2.py < input-1.dat > output-1.dat

clean:
	rm -rf __pycache__ *.pyc
