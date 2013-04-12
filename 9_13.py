#!/usr/bin/python
#encoding: utf-8
#code/setdict/birdwatching.txt

import sys

def count_birds():
    '''Count all the birds.'''
    count = {}
    for filename in sys.argv[1:]:
        infile = open(filename, 'r')
        for line in infile:
            name = line.strip()
            count[name] = count.get(name, 0) + 1

        infile.close()

    return count


def print_dict(freq):
    '''Print.'''
    for key in sorted(freq):
        print key
        for name in freq[key]:
            print ' ', name


def invert_dict():
    '''Invert the dictionary.'''
    count = count_birds()

    freq = {}
    for (name, times) in count.items():
        if times in freq:
            freq[times].append(name)
        else:
            freq[times] = [name]

    print_dict(freq)


invert_dict()


