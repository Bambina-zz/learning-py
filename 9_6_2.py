#!/usr/bin/python
#encoding: utf-8

input = {'ニュートロン':0.55, '陽子':0.21, '中間子':0.03, 'ミューオン':0.07, 'ニュートリノ':0.14}

def find_lowestElem(input):
    '''最小値を更新していく'''
    least_val = None
    least_key = None

    for key in input:
        if least_val is None:
            least_val = input[key]
            least_key = key
        elif least_val > input[key]:
            least_val = input[key]
            least_key = key

    return least_key

print find_lowestElem(input)


