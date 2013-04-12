#!/usr/bin/python
#encoding: utf-8

input = {'seiya':{'height':178,'weight':70,'age':26},
         'mayuk':{'height':170,'weight':57,'age':24}}

def db_headings(input):
    '''内側の辞書で使われているキーの集合を返す'''
    inner_keys = set()
    for key in input:
        for inner_key in input[key]:
            inner_keys.add(inner_key)

    return inner_keys

print db_headings(input)

