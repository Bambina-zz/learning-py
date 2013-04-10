#!/usr/bin/python

#引数ファイルの形式:author xxxxxxxが0行以上

def find_author(input_file):
    '''引数ファイルの作者リストから全ての作者名を取り出して集合をつくる'''
    authors = set()
    for line in input_file:
        line = line.split()
        authors.add(line[1])

    return authors

if __name__ == '__main__':
    import sys
    input_file = open(sys.argv[1], 'r')
    print find_author(input_file)
    input_file.close()

