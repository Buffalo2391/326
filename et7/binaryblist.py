'''COSC326 Levi Faid 3894507 Tommy Chen 5277929 Python 3.6.2 Etude 7'''
from sys import stdin
import re
import sys
import math
import queue
import time
import copy

wordchart = list()
connections = list()
class Tree:
    def __init__(self, single):
        self.nodes = {}
        self.word = None
        self.single = single       
        self.parent = None
    def addernode(self, final, wrdsheet):
        finalwordchart = list(wrdsheet)
        binarywordchart = list(wrdsheet)
        wlen = len(self.word)
        if(self.parent==None and self.isConnected(self.word, final)):
            connections.append(final)
            connections.append(self.word)
            return list()
        bchart = list()
        for i in range(wlen):
            if i==0 or (self.single == False and i < int(wlen/2)):
                 continue           
            match = self.binarySearch(self.word[-i:], binarywordchart)
            while(match!=None):
                
                bchart.append(binarywordchart[match])
                del binarywordchart[match]
                match = self.binarySearch(self.word[-i:], binarywordchart)

        for word in bchart:
            if(self.isConnected(self.word, word)):                    
                thing = Tree(self.single)
                thing.word = word
                thing.parent = self
                self.nodes[word] = thing
                finalwordchart.remove(word)
                if thing.isConnected(thing.word, final) :
                    connections.append(final)
                    connections.append(thing.word)
                    obj = self     
                    while(obj.parent!=None):
                        connections.append(obj.word)
                        obj = obj.parent
                    connections.append(obj.word)
                    return list()
        return finalwordchart
        




    def binarySearch(self, word, wordlist):        
        start = 0
        end = len(wordlist) - 1
        wordLength = len(word)
        while(start <= end):
            mid = int((start + end)/2)
            midw = wordlist[mid][:wordLength]
            if (word > midw):
                start = mid + 1                   
            elif(word < midw):
                end = mid - 1
            else:
                return mid     
        return None

        
    def isConnected(self, frt, scd):
        if len(scd) > len(frt):
            lowLen = len(frt)
        else:
            lowLen = len(scd)
        if(self.single):
            ConnectionMinimum = int(lowLen/2)+(lowLen%2)
        else:
            ConnectionMinimum = math.ceil((len(frt) if lowLen!=len(frt) else len(scd))/2)
        for i in range(ConnectionMinimum, lowLen+1):            
            if(frt[-i:]==scd[:i]):
                return True
        return False
        


                
lines = stdin.readlines()
verystart = time.time()
for line in lines:
    if(not re.search('^#', line, flags=0)):
        line = line.strip()
        item = re.split(' ',line, flags=0)
        for thing in item:
            if(None!=re.search('^[a-zA-Z]+$', thing, flags=0)):
                wordchart.append(thing)
wordchart.sort()
word1 = sys.argv[1]
word2 = sys.argv[2]
if(word1 == word2):
    print("1 %s" % word1)
    print("1 %s" % word1)
else:
    for value in (True, False):

        connections.clear()
        root = Tree(value)
        root.word = word1
        final = word2
        innerwordchart = root.addernode(final, wordchart)
        nodeQueue = queue.Queue()   
        for item in sorted(root.nodes):
            nodeQueue.put(root.nodes[item])        
        while((not nodeQueue.empty()) and 0 == len(connections)):
            node = nodeQueue.get()            
            innerwordchart = node.addernode(final, innerwordchart)
            for item in sorted(node.nodes):
                nodeQueue.put(node.nodes[item])
            if(len(node.nodes)==0):
                del(node)
        print(time.time()-verystart)
        connections.append(str(len(connections)))
        print(' '.join(reversed(connections)))
