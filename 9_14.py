#!/usr/bin/python
#encoding: utf-8

#[0,0,0,4,0,6,7,0,0,0] => {3:4,5:6,6:7}
#[0,0,0,1,0,0,3,0,1,1] => {3:1,6:3,8:1,9:1}

v1 = {3:4,5:6,6:7}
v2 = {3:1,6:3,8:1,9:1}

def sum_vector(v1,v2):
    result = v2.copy()
    for key in v1:
        if key in result:
            result[key] = result[key] + v1[key]
        else:
            result[key] = v1[key]

    print result

sum_vector(v1,v2)
