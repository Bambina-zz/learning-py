#!/usr/bin/python
#encoding: utf-8

#引数に辞書を取り、最も低いvalのkeyを返す

input = {'ニュートロン':0.55, '陽子':0.21, '中間子':0.03, 'ミューオン':0.07, 'ニュートリノ':0.14}

def find_lowestElem(input):
    probs = input.values()
    min_probs = min(probs)
    freq = {}

    for (name, prob) in input.items():
        if prob in freq:
            freq[prob].append(name)
        else:
            freq[prob] = [name]

    print str(freq[min_probs])

find_lowestElem(input)

