'''COSC326 Levi Faid 3894507 Python 3.6.2 Etude 10'''
from sys import stdin
import re
import math

greenchart = {1:True, 2:False}

def whatcolour(value):
    if(value in greenchart):
        return greenchart[value]
    else:
        gtotal = 0
        rtotal = 0
        nfactors = nearfactors(value)
        for n in nfactors:
            if(whatcolour(int(n)) == True):
                gtotal += 1
            else:
                rtotal += 1
        if(gtotal > rtotal):
            greenchart[value] = False
            return False
    greenchart[value] = True
    return True

#fills in the look up table up to the limit required
def nearfactors(value):
    kvalues = {1}
    x = 2
    i = math.floor(value/x)
    while i > 1:
        k = math.floor(value/i)
        kvalues.add(k)
        x = k+1
        i = math.floor(value/x)
    return kvalues
'''
checks if the upper limit has been reached before, if not fills in the chart
and then it making a string of G or R based on the two givin values
'''
def rgprinter(a, b):
    printedvalue = '#'
    for x in range(a,a+b):
        if(whatcolour(x) == True):
            printedvalue += 'G'
        else:
            printedvalue += 'R'
    return printedvalue

#Reads lines in and if the conform with the style inact the redgreening
lines = stdin.readlines()
for line in lines:
    if(not re.search('^#', line, flags=0)):
        print(line)
        if(re.search('[0-9]+ [0-9]+', line, flags=0)):
            values = re.split(' ', line, flags=0)
            print(rgprinter(int(values[0]), int(values[1])))

