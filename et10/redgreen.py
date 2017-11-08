'''COSC326 Levi Faid 3894507 Python 3.6.2 Etude 10'''
from sys import stdin
import re
import math

greenchart = []
greenchart.append(True)
greenchart.append(False)

#fills in the look up table up to the limit required
def fillvalues(limit):
    for index in range(1, int(limit)+1):
        if(len(greenchart)<index):
            kvalues = {1}
            greenchart.append(True)
            for i in range(2, int((index)/2)+3):
                k = math.floor(index/i)
                kvalues.add(k)
            rtotal = 0
            gtotal = 0
            for k in kvalues:
                if greenchart[k-1] == True:
                    gtotal += 1
                else:
                    rtotal += 1
            if(gtotal>rtotal):
                greenchart[index-1] = False
'''
checks if the upper limit has been reached before, if not fills in the chart
and then it making a string of G or R based on the two givin values
'''
def rgprinter(a, b):
    printedvalue = ''
    if(len(greenchart)<(a+b-1)):
        fillvalues(int(a)+int(b)-1)
    for x in range(a,a+b):
        if(greenchart[x-1] == True):
            printedvalue += 'G'
        else:
            printedvalue += 'R'
    print(printedvalue)
#Reads lines in and if the conform with the style inact the redgreening
lines = stdin.readlines()
for line in lines:
    if(re.search('[0-9]+ [0-9]+',line,flags=0)):
       values = re.split(' ', line,flags=0)
       print('%s %s' % (values[0], values[1]))
       rgprinter(int(values[0]), int(values[1]))
