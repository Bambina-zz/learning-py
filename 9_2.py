#!/usr/bin/python
#encoding: utf-8

#./9_2.py a-b-c-d 1-2-3-4

def mating_pairs(f_list, m_list):
    '''同じサイズの2つの集合から対の集合を返す'''
    females = set(f_list.split('-'))
    males = set(m_list.split('-'))

    while males and females:
        tmp_pair = set()
        tmp_pair.add((males.pop(),females.pop()))
        print tmp_pair

if __name__ == "__main__":
    import sys
    f_list = sys.argv[1]
    m_list = sys.argv[2]
    mating_pairs(f_list, m_list)
