# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:56:30 2022

@author: Nicklas Branding
"""
data = 'adventofcode4.txt'

pair1 = []
pair2 = []
pair1_val1 = []
pair1_val2 = []
with open(data, 'r') as f:
    lines = f.readlines()
    print(lines)
    
    pairs = [[s for s in i.split(',')] for i in lines]
    pairs = [[[int(e.split('-')[0]), int(e.split('-')[1])] for e in p] for p in pairs]
    print(pairs)
    
def contains( e0, e1):
    ass_pair=0
    if (e0[0]<=e1[0]) and (e0[1]>=e1[1]):
        print(e0[0])
        print(e1[0])
        print(e0[1])
        print(e1[1])
        return True
    elif (e1[0]<=e0[0]) and (e1[1]>=e0[1]):
        print(e0[0])
        print(e1[0])
        print(e0[1])
        print(e1[1])
        return True
    else:
        return False
def overlap( e0, e1):
    ass_pair=0
    if (e0[0]<=e1[0]) and (e0[1]>=e1[0]):
        print(e0[0])
        print(e1[0])
        print(e0[1])
        print(e1[1])
        return True
    elif (e1[0]<=e0[0]) and (e1[1]>=e0[0]):
        print(e0[0])
        print(e1[0])
        print(e0[1])
        print(e1[1])
        return True
    else:
        return False

print(sum([contains(*p) for p in pairs]))    
print(sum([overlap(*p) for p in pairs])) 