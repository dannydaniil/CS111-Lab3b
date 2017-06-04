#!usr/bin/python

import sys, string, math

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
    lists = [[] for i in range(7)]
    with open(fs_csv, 'r') as csv:
        for line in csv:
            line = line.replace('\n', '')
            summary_line = line.split(',')
            try:
                index = indices[summary_line[0]]
            except KeyError:
                print >> sys.stderr, "{0} {1}".format("Error: Invalid first entry:",
                        summary_line[0])
                sys.exit(1)
            lists[index].append(summary_line)
    return lists

def check_invalid_blocks(lists):
    num_blocks = int(lists[1][0][2])
    reserved_blocks = [1, 2]
    reserved_blocks.append(int(lists[1][0][6]))
    reserved_blocks.append(int(lists[1][0][7]))
    inode_blocks = int(math.ceil(float(lists[0][0][4]) * float(lists[1][0][3]) / float(lists[0][0][3])))
    reserved_blocks += range(int(lists[1][0][8]), int(lists[1][0][8]) + inode_blocks)

    #TODO: find invalid inodes ?
    num_inodes = lists[0][0][2]
    
    dict = {
        1: "INDIRECT BLOCK",
        2: "DOUBLE INDIRECT BLOCK",
        3: "TRIPPLE INDIRECT BLOCK"
    }

    indirection_offset = {
        1: 12,
        2: 268,
        3: 65804
    }

    for inode in lists[4]:
        for i in range(12, len(inode)):
            if int(inode[i]) == 0:
                continue
            if int(inode[i]) in reserved_blocks:
                if i < 24:
                    print "RESERVED BLOCK {0} IN INODE {1} AT OFFSET {2}".format(inode[i], inode[1], i - 12)
                else:
                    indirection_level = i - 23
                    try:
                        print "RESERVED {0} {1} IN INODE {2} AT OFFSET {3}".format(dict[indirection_level], inode[i], inode[1], indirection_offset[indirection_level])
                    except KeyError:
                        print >> sys.stderr, "Error: Invalid indirection level"
                        sys.exit(1)
            if int(inode[i]) > num_blocks:
                if i < 24:
                    print "INVALID BLOCK {0} IN INODE {1} AT OFFSET {2}".format(inode[i], inode[1], i - 12)
                else:
                    indirection_level = i - 23
                    try:
                        print "INVALID {0} {1} IN INODE {2} AT OFFSET {3}".format(dict[indirection_level], inode[i], inode[1], indirection_offset[indirection_level])
                    except KeyError:
                        print >> sys.stderr, "Error: Invalid indirection level"
                        sys.exit(1)
    '''
    for indirect in lists[6]:
        if int(indirect[5]) > num_blocks:
            try:
                print "RESERVED {0} {1} IN INODE {2} AT OFFSET {3}".format(dict[indirect[2]], indirect[5], indirect[1], indirect[3])
            except KeyError:
                print >> sys.stderr, "Error: Invalid indirection level"
                sys.exit(1)

        if int(indirect[5]) > num_blocks:
            try:
                print "INVALID {0} {1} IN INODE {2} AT OFFSET {3}".format(dict[indirect[2]], indirect[5], indirect[1], indirect[3])
            except KeyError:
                print >> sys.stderr, "Error: Invalid indirection level"
                sys.exit(1)
    '''

def main():
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: python2 lab3b.py fs_report.csv"
        sys.exit(1)
    fs_csv = sys.argv[1]
    lists = parse_csv(fs_csv)
    check_invalid_blocks(lists)

if __name__ == "__main__":
    main()

