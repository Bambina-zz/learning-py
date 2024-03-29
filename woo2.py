#!/usr/bin/python

import sys

def read_housing_data(r):
    starts = []
    contracts = []
    rates = []

    for line in r:
        start, contract, rate = line.split()
        starts.append(float(start))
        contracts.append(float(contract))
        rates.append(float(rate))

    return (starts, contracts, rates)

def process_housing_data(starts, contracts):
    return (sum(starts[12:24]) - sum(starts[0:12]), sum(contracts[12:24]) - sum(contracts[0:12]))



if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    starts, contracts, rates = read_housing_data(input_file)
    print process_housing_data(starts, contracts)
    input_file.close()

