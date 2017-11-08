'''COSC326 Levi Faid 3894507 Tommy Chen 5277929 Python 3.6.2 Etude 7'''
from sys import stdin
import re
import sys
import math
import queue
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
        WordLength = len(self.word)        
        if(self.parent==None):
            nothing = True
            if self.isConnected(self.word, final) :
                connections.append(final)
                connections.append(self.word)
                return list()
            for word in wrdsheet:
                if self.isConnected(word, final):
                    if(word!=final):
                        nothing = False
                    
            if nothing:
                return list()
        if self.single :
            for i in range(WordLength):
                MatchString = self.word[i:]
                binarywordchart = list(finalwordchart)
                MatchAddress= self.binarySearch(MatchString, binarywordchart)
                while(MatchAddress!= None):
                    word = str(binarywordchart[MatchAddress])
                    if (len(MatchString) >= min(math.ceil(WordLength/2), math.ceil(len(word)/2))):  
                        thing = Tree(self.single)
                        thing.word = word
                        thing.parent = self
                        self.nodes[word] = thing
                        match2 = self.binarySearch2(word, finalwordchart)                        
                        del finalwordchart[match2]
                        if thing.isConnected(thing.word, final) :                                
                            connections.append(final)
                            connections.append(thing.word)
                            obj = self     
                            while(obj.parent!=None):
                                connections.append(obj.word)
                                obj = obj.parent
                            connections.append(obj.word)
                            return list()
                    del binarywordchart[MatchAddress]
                    MatchAddress= self.binarySearch(MatchString, binarywordchart)

        else :
            
            for i in range(WordLength):
                MatchString = self.word[i:]  
                if (len(MatchString) < math.ceil(WordLength/2)):
                     continue
                              
                binarywordchart = list(finalwordchart)
                MatchAddress= self.binarySearch(MatchString, binarywordchart)
                
                while(MatchAddress!=None):
                    word = str(binarywordchart[MatchAddress])
                    
                    if len(MatchString) >= math.ceil(len(word)/2) :
                        
                        thing = Tree(self.single)
                        thing.word = word
                        thing.parent = self
                        self.nodes[word] = thing
                        match2 = self.binarySearch2(word, finalwordchart)                        
                        del finalwordchart[match2]
                        if thing.isConnected(thing.word, final) :
                            connections.append(final)
                            connections.append(thing.word)
                            obj = self     
                            while(obj.parent!=None):
                                connections.append(obj.word)
                                obj = obj.parent
                            connections.append(obj.word)
                            return list()
                        
                    del binarywordchart[MatchAddress]
                    
                    MatchAddress= self.binarySearch(MatchString, binarywordchart)
                    
                
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

    def binarySearch2(self, word, wordlist):        
        start = 0
        end = len(wordlist) - 1
        wordLength = len(word)
        while(start <= end):
            mid = int((start + end)/2)
            midw = wordlist[mid]
            if (word > midw):
                start = mid + 1                   
            elif(word < midw):
                end = mid - 1
            else:
                return mid     
        return None
        
    def isConnected(self, frt, scd):
        lowLen = len(frt) if len(scd) > len(frt) else len(scd)
        if(self.single):
            ConnectionMinimum = math.ceil(lowLen/2)
        else:
            ConnectionMinimum = math.ceil((len(frt) if lowLen!=len(frt) else len(scd))/2)
        for i in range(ConnectionMinimum, lowLen+1):
            word = frt[-i:]
            if(word==scd[:len(word)]):
                return True
        return False
        


                
lines = stdin.readlines()

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
        connections.append(str(len(connections)))
        print(' '.join(reversed(connections)))
