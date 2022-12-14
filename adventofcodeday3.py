# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:49:33 2022

@author: Nicklas Branding
"""
import textwrap
data = 'data.txt'
newList = []
listSize = []
with open(data) as f:
    lines = f.readlines()
    print(lines)

    sum_pri = 0
    for line in lines:
        i = len(line)
        pocket1 = line[0:int(i/2)]
        pocket2 = line[int(i/2):i]
        print(pocket1)
        print(pocket2)
        for duplicate_char in pocket1:
            if duplicate_char in pocket2:
                sum_pri += (ord(duplicate_char)- 38 if duplicate_char.isupper() else ord(duplicate_char) - 96)
                break
    print(sum_pri)
    
    sum_pri = 0
    for i in range(0, len(lines), 3):
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2]:
                sum_pri += (ord(c) - 38 if c.isupper() else ord(c) - 96)
                break
    print(sum_pri)
        