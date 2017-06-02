#!usr/bin/python

import sys, string,argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_system")
args = parser.parse_args()
print args.file_system
