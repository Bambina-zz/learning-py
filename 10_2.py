#!/usr/bin/python
#encoding: utf-8

sequence = [4,37,12,82,68,8,69,35,2,34,6]

def min_index(sequence):
    '''1パスでリスト内の最小値と添字を取得するループ'''
    freq_min = sequence[0]

    for i,data in enumerate(sequence):
        if data < freq_min:
            index = i
            freq_min = data

    return (freq_min,index)

print min_index(sequence)
