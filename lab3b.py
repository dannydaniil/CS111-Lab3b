#!usr/bin/python

import sys, string

<<<<<<< HEAD
def test(file_system):
    print file_system

def main():
    file_system = ""
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: python2 lab3b.py file_system"
    else:
        file_system = sys.argv[1]
        print file_system
    test(file_system)

if __name__ == "__main__":
    main()
=======



def main():
    print sys.argv[1]


main()
>>>>>>> 4d4d63517ac6e972a5f5eecdba94afa68a2c592c
