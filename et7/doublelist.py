'''COSC326 Levi Faid 3894507 Tommy Chen 5277929 Python 3.6.2 Etude 7'''
from sys import stdin
import re
import sys
import math
import queue
import copy
import time
wordchart = list()
wordc = [[] for _ in range(26)]
connections = list()
class Tree:
    def __init__(self, single):
        self.nodes = {}
        self.word = None
        self.single = single       
        self.parent = None
    def addernode(self, final, wrdsheet):
        finalwordchart = copy.deepcopy(wrdsheet)
        if(self.parent==None):            
            if self.isConnected(self.word, final) :
                connections.append(final)
                connections.append(self.word)
                return wordchart
            for word in wrdsheet:
                if self.isConnected(word, final):
                    break
        for i in range(0, int(len(self.word))):
            if self.single == False and i < int(len(self.word)/2) :
                continue
            indw = int(ord(self.word[i])-97)
            for word in wrdsheet[indw]:
                if(self.isConnected(self.word, word)):
                    thing = Tree(self.single)
                    thing.word = word
                    thing.parent = self
                    self.nodes[word] = thing
                    if word in finalwordchart[int(ord(word[0])-97)]:
                        finalwordchart[int(ord(word[0])-97)].remove(word)
                    if(thing.isConnected(word, final)):
                        connections.append(final)
                        connections.append(word)
                        obj = self     
                        while(obj.parent!=None):
                            connections.append(obj.word)
                            obj = obj.parent
                        connections.append(obj.word)
                        return finalwordchart
        
        return finalwordchart

    def isConnected(self, frt, scd):
        if len(scd) > len(frt):
            lowLen = len(frt)
            frtL = True
        else:
            lowLen = len(scd)
            frtL = False
        if(self.single):
            ConnectionMinimum = int(lowLen/2)+(lowLen%2)
        else:
            ConnectionMinimum = math.ceil((len(frt) if lowLen!=len(frt) else len(scd))/2)
        for i in range(ConnectionMinimum, lowLen+1):            
            if(frt[-i:]==scd[:i]):            
                return True


                
lines = stdin.readlines()
for line in lines:
    if(not re.search('^#', line, flags=0)):
        line = line.strip()
        item = re.split(' ',line, flags=0)
        for thing in item:
            if(None!=re.search('^[a-zA-Z]+$', thing, flags=0)):
                wordchart.append(thing)
                ind = ord(thing[0])-97
                wordc[ind].append(thing)


wordchart.sort()
word1 = sys.argv[1]
word2 = sys.argv[2]
if(word1 == word2):
    print("1 %s" % word1)
    print("1 %s" % word1)
else:
    for value in (True, False):
        start = time.time()
        connections.clear()
        root = Tree(value)
        root.word = word1
        final = word2
        innerwordchart = root.addernode(final, wordc)
        nodeQueue = queue.Queue()       
        
        for item in sorted(root.nodes):
            nodeQueue.put(root.nodes[item])        
        while((not nodeQueue.empty()) and 0 == len(connections)):
            node = nodeQueue.get()            
            innerwordchart = node.addernode(final, innerwordchart)            
            for item in sorted(node.nodes):
                nodeQueue.put(node.nodes[item])
        connections.append(str(len(connections)))
        print(' '.join(reversed(connections)))
        print(time.time()-start)
