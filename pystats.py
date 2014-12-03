#!/usr/bin/env python

# Author: Zhonghua Xi
# Date: 12/3/2014

import sys

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

def stats(stream, field=1, d=' '):
    data = []
    for line in stream:
        items = line.split(d)
        data.append(float(items[field-1]))

    s = sum(data)
    m = mean(data, s)
    v = variance(data, m)

    print_st("Field", field)
    print_st("Lines", len(data))
    print_st("Mean", m)
    print_st("Variance", v)
    print_st("StdDev", v ** 0.5)
    print_st("Sum", s)
    print_st("Min", min(data))
    print_st("Max", max(data))
    print_st("Median", median(data))

if  __name__ == "__main__":
    stats(sys.stdin)