#!/usr/bin/python
#encoding: utf-8

v1 = {3:4,5:6,6:7}
v2 = {3:1,6:3,8:1,9:1}

def sparse_dot(v1,v2):
    '''2つのベクトルの積の和を返す'''
    freq = {}

    for key in v1:
        if key in v2:
            freq[key] = v1[key] * v2[key]

    return freq

print sparse_dot(v1,v2)
