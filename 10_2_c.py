#!/usr/bin/python
#encoding: utf-8

def min_or_max_index(sequence, bool):
    '''boolがTrueなら最小、Falseなら最大、の値と添字を返す'''
    freq = sequence[0]

    if bool == 'True':
        for i,data in enumerate(sequence):
            if data < freq:
                freq = data
                index = i
    elif bool == 'False':
        for i,data in enumerate(sequence):
            if data > freq:
                freq = data
                index = i

    print (freq, index)

if __name__ == '__main__':
    import sys
    bool = sys.argv[1]
    sequence = [4,37,12,82,68,8,69,35,2,34,6]
    min_or_max_index(sequence, bool)

