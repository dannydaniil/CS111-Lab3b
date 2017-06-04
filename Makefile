.SILENT:

TAR = lab3b-504636684.tar.gz
FILES = Makefile README lab3b.py lab3b
CC = python

default:  lab3b

lab3b:
	chmod u+x lab3b lab3b.py
	$(CC) lab3b.py

clean:

dist:
	tar cfv $(TAR) $(FILES)
