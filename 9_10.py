#!/usr/bin/python
#encoding: utf-8

dic_1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
dic_2 = {'a':1,'c':3,'e':5,'g':7,'i':9}

def dict_intersect(dic_1,dic_2):
    intersec = {}

    for key in dic_1:
        if (key in dic_2) and (dic_1[key] == dic_2[key]):
            intersec[key] = dic_1[key]

    return intersec

print dict_intersect(dic_1,dic_2)

