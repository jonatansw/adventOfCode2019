# -*- coding: utf-8 -*-
"""
Created on Mon Dec 02 11:35:33 2019

@author: jonatan.willners
"""

def inp(Id, List):
    if List[Id]==1: 
        List[List[Id+3]] = List[List[Id+1]] + List[List[Id+2]]
        return False
    elif List[Id]==2:
        List[List[Id+3]] = List[List[Id+1]] * List[List[Id+2]]
        return False
    elif List[Id]==99:
        return True

L = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
for i in range(0, len(L), 4):
    done = inp(i, L)
    
print L[0]
#B
for a in range(100):
    for b in range(100):
        L = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
        L[1] = a
        L[2] = b
        for i in range(0, len(L), 4):
            done = inp(i, L)
            if done: break
        done = L[0] == 19690720;
        if done: break
    if done: break
print L[1]*100+L[2]