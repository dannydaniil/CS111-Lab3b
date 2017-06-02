#!usr/bin/python

import sys, string, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_system")
    args = parser.parse_args()
    print args.file_system

if __name__ == "__main__":
    main()
