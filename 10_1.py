#!/usr/bin/python
#encoding: utf-8

#DNAシーケンスの補数を返す
#A-T  G-C

#補数を入れるリストresult[]を用意する
#引数(リスト)の各要素を順番に解析する
#もしAならT、TならA、GならC、CならGをresult[]に追加する
#result[]を返す

sequence = ['A','A','T','T','G','C','C','G','T']

def complement(sequence):
    result = []

    for base in sequence:
        if base == 'A':
            result.append('T')
        elif base == 'T':
            result.append('A')
        elif base == 'G':
            result.append('C')
        elif base == 'C':
            result.append('G')

    print result

complement(sequence)
