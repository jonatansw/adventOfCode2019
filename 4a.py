# -*- coding: utf-8 -*-
"""
Created on Wed Dec 04 06:28:15 2019

@author: jonatan.willners
"""

def validityCheck(inp):
    double = False
    for i in range(1, len(inp)):
        if inp[i] < inp[i-1]:
            return 0
        elif inp[i] == inp[i-1]:
            double = True
    return int(double)


def validityCheck2(inp):
    if validityCheck(inp):
        for c in inp:      
            if inp.count(c)==2:
                return True
    return 0
s1, s2 = 0, 0
for i in range(136818, 685979+1):
   s1+=validityCheck(str(i))
   s2+=validityCheck2(str(i))
print s1, s2
