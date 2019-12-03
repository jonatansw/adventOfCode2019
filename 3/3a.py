# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 08:44:59 2019

@author: jonatan.willners
"""
import numpy as np
Movement = {'L' : np.array([-1, 0]),
            'R' : np.array([1, 0]),
            'U' : np.array([0, 1]),
            'D' : np.array([0, -1])}

def addMovement(List, wire):
    x, y= 0,0
    length = 0
    for inp in wire:
        for i in range(int(inp[1:])):
            length +=1
            x += Movement[inp[0]][0]
            y += Movement[inp[0]][1]
            List[(x, y)] = [abs(x)+abs(y), length]
    
    
w1 = {}
w2 = {}
addMovement(w1, open('wire1.txt', 'r').read().split(','))
addMovement(w2, open('wire2.txt', 'r').read().split(','))

minV = float('inf')
for key, value in w1.items():
    if w2.has_key(key):
        if value[0] < minV:
            minV = value[0]
print minV

minV = float('inf')
for key, value in w1.items():
    if w2.has_key(key):
        if value[1]+w2[key][1] < minV:
            minV = value[1]+w2[key][1]
print minV

