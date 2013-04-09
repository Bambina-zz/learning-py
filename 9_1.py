#!/usr/bin/python

def find_dups(num_list):
'''引数のリストから重複アイテムを取り出す'''
    a = []
    dups = []

    for n in num_list:
        if n in a:
            dups.append(n)
        else:
            a.append(n)

    print set(dups)

if __name__ == '__main__':
    import sys
    num_list = sys.argv[1:]
    find_dups(num_list)

