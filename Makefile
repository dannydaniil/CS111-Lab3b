.SILENT:

TAR = lab3b-504636684.tar.gz
FILES = Makefile README lab3b.py
CC = python

default:  lab3a

lab3a:
	$(CC) lab3b.py

clean:
	rm -rf report.csv

dist:
	tar cfv $(TAR) $(FILES)
