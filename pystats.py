#!/usr/bin/env python

# Author: Zhonghua Xi
# Date: 12/3/2014

import sys

VERSION = "0.0.2"

def print_help():
    print 'pystats - a summary statistics script'
    print 'Version', VERSION, 'by Zhonghua Xi'
    print 'Project website: https://github.com/xizhonghua/pystats'
    print 'Usage:',sys.argv[0],'[options]'
    print 'Options:'
    print '    -h  ', 'help message'
    print '    -f# ', 'field index, start from 1'
    print '    -d# ', 'field delimiter'
    print '    -s#', 'skip first # lines, default is one for header'


def parse_args():
    delimiter = ' '
    field = 1
    i = 1
    skip = 0
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg[0] != '-':
            print 'unknown option:', i
            sys.exit(0)
        if arg == '-h':
            print_help()
            sys.exit(0)
        elif arg.startswith('-f'):
            field = int(arg[2:])
        elif arg.startswith('-d'):
            delimiter = (arg[2:])
        elif arg.startswith('-s'):
            skip = 1 if arg == '-s' else int(arg[2:])
        i+=1
    return (field, delimiter, skip)

def mean(data, s = None):
    if len(data) == 0:
        return 0

    # use pre-computed sum if we have it
    ss = sum(data) if s == None else s

    m = ss / float(len(data))

    return m

def variance(data, miu = None):
    if len(data) == 0:
        return 0
    # use pre-computed miu
    m = mean(data) if miu == None else miu
    v = sum((m - value) ** 2 for value in data) / float(len(data))
    return v

def median(data):
    if len(data) == 0:
        return 0

    mid = len(data)/2

    if len(data)%2==0: 
        return (data[mid] + data[mid-1])/2

    return data[mid]


def print_st(key, value):
    print key.rjust(12, '_') , '=', value

def stats(stream, field=1, delimiter=' ', skip = 0):
    data = []
    lineNum = 0
    for line in stream:

        lineNum += 1

        # skip first skip lines
        if lineNum <= skip: continue

        # if line is empty or white space, do nothing
        if len(line) == 0 or line.isspace(): continue

        items = line.split(delimiter)
        data.append(float(items[field-1]))

    s = sum(data)
    m = mean(data, s)
    v = variance(data, m)
    min_value = 0 if len(data) == 0 else min(data)
    max_value = 0 if len(data) == 0 else max(data)

    print_st("Field", field)
    print_st("Lines", len(data))
    print_st("Mean", m)
    print_st("Variance", v)
    print_st("StdDev", v ** 0.5)
    print_st("Sum", s)
    print_st("Min", min_value)
    print_st("Max", max_value)
    print_st("Median", median(data))

if  __name__ == "__main__":
    field, delimiter, skip = parse_args()
    stats(sys.stdin, field, delimiter, skip)