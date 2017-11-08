'''COSC326 Levi Faid 3894507 Python 3.6.2 Etude 10'''
from sys import stdin
import re
import math
import time

nftime = 0.0

#fills in the look up table up to the limit required
def nearfactors1(value):
    kvalues = {1}
    x=2
    i=math.floor(value/x)
    while i>1:
        k=math.floor(value/i)
        kvalues.add(k)
        x=k+1
        i=math.floor(value/x)
    return sorted(kvalues)

def nearfactors2(value):
    
    kvalues = {1}
    x=2
    i=math.floor(value/x)
    while i>1:        
        k=math.floor(value/i)
        kvalues.add(k)
        x+=1
        i=math.floor(value/x)
    return sorted(kvalues)

def nearfactors3(value):
    multivalues = 0
    kvalues = {1}
    for i in range(2, value):
        k=math.floor(value/i)
        if k not in kvalues:
            kvalues.add(k)
        else:
            multivalues+=1
    #print(multivalues)
    return sorted(kvalues)

tests = (8, 74, 100, 1000, 10000, 100000)
for x in tests:
    
    if not (nearfactors1(x)==nearfactors2(x)==nearfactors3(x)):
        print(x)
        print(nearfactors1(x))
        print(nearfactors2(x))
        print(nearfactors3(x))
