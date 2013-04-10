#!/usr/bin/python
#encoding: utf-8


#引数に辞書が渡されると、辞書の値の数を返す
#{'赤':1, '青':1, '緑':2, '黄':3}

library = {'赤':1, '青':1, '緑':2, '黄':3}
vals = set()

def count_val(library):
    for i in library:
        vals.add(library[i])

    print len(vals)

count_val(library)

