#!/usr/bin/python

def read_data(r):
    fields = ((4, int),(2,int), (2,int))
    result = []

    for line in r:
        start = 0
        record = []
        for (width, target_type) in fields:
            text = line[start:start+width]
            field = target_type(text)
            record.append(field)
            start += width

        result.append(record)

    return result

