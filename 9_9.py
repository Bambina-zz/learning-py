#!/usr/bin/python
#encoding: utf-8


def is_balanced(r_val,g_val,b_val):
    input = {'R':r_val,'G':g_val,'B':b_val}
    val_list = input.values()

    sum = 0
    for n in val_list:
        sum += float(n)

    if sum == 1.0:
        print 'true'

if __name__ == '__main__':
    import sys
    r_val = sys.argv[1]
    g_val = sys.argv[2]
    b_val = sys.argv[3]
    is_balanced(r_val,g_val,b_val)
