#!/usr/bin/python
#encoding: utf-8

input = {'seiya':{'height':178,'weight':70,'age':26},
         'mamas':{'height':164,'weight':50,'age':50},
#         'papas':{'height':164,'weight':50,'age':50,'sex':1},
         'mayuk':{'height':170,'weight':57,'age':24}}

def first_dict_key(input):
    '''一つ目の辞書の内側で使われているキーの集合を返す'''
    keys = input.keys()
    first_key_set = set()

    for key in input[keys[0]]:
        first_key_set.add(key)

    return first_key_set


def db_consistent(input):
    sample_set = first_dict_key(input)

    for key in input:
        for inner_key in input[key]:
            if inner_key not in sample_set:
                return 'false'

    return 'true'

print db_consistent(input)
