#!/usr/bin/python
#encoding: utf-8


def fetch_and_set(Key,new_value):
    '''引数にKeyとnew_valueを取り、辞書にkeyがあれば、値を返しnew_valueに置き換え、Keyがなければエラーメッセージを返す'''

    input = {'egg':1,'rabbit':2,'tometo':3,'bird':4}

    if input.has_key(Key):
        print input[Key]
        input[Key] = new_value
        print input
    else:
        print 'Unable to replace value for nonexistent key'

if __name__ == '__main__':
    import sys
    Key = sys.argv[1]
    new_value = sys.argv[2]
    fetch_and_set(Key,new_value)
