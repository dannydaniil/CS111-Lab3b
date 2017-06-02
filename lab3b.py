#!usr/bin/python

import sys, string
def test(file_system):
    print file_system

def main():
    file_system = ""
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: python2 lab3b.py file_system"
        sys.exit(1)
    else:
        file_system = sys.argv[1]
        print file_system
    test(file_system)

if __name__ == "__main__":
    main()

