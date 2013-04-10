#!/usr/bin/python
#encoding: utf-8

input = {'にんじん':1,'じゃがいも':1,'たまねぎ':0.5,'牛肉':150,'オリーブオイル':0.5,'ルー':4}

def count_diplicates(input):
    '''引数として辞書を取り、複数回現れる値の数を返す'''
    dip_counter = 0
    freq = []
    vals = set()

    for key in input:
        if input[key] in freq:
            vals.add(input[key])
        else:
            freq.append(input[key])

    return len(vals)

print count_diplicates(input)

