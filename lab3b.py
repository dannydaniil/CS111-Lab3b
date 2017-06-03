#!usr/bin/python

import sys, string

def test(file_system):
    print file_system
def parse_csv(fs_csv):
    indices = {
        "SUPERBLOCK": 0,
        "GROUP": 1,
        "BFREE": 2,
        "IFREE": 3,
        "INODE": 4,
        "DIRENT": 5,
        "INDIRECT": 6
    }
    lists = []
    for i in range(7):
        lists.append([])
    with open(fs_csv, 'r') as csv:
        for line in csv:
            summary_line = line.split(',')
            try:
                index = indices[summary_line[0]]
            except KeyError:
                print >> sys.stderr, "{} {}".format("Error: Invalid first entry:",
                        summary_line[0])
                sys.exit(1)
            lists[index].append(summary_line)
    return lists


def main():
    file_system = ""
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: python2 lab3b.py file_system"
        sys.exit(1)
    else:
        fs_csv = sys.argv[1]
        print fs_csv
    lists = parse_csv(fs_csv)
    print lists


if __name__ == "__main__":
    main()
