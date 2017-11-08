##Etude 9 Sir Tets Carpet python 3.6.2
##Levi Faid, Daniel Thomson, Rebecca Wilson, Nathan Hardy

from sys import stdin
import re
#Tiles 
allTetrominos = []
allTetrominos.append(((0,0),(1,0),(2,0),(3,0)))
allTetrominos.append(((0,0),(0,1),(0,2),(0,3)))
allTetrominos.append(((0,0),(1,0),(2,0),(2,1)))
allTetrominos.append(((0,0),(1,0),(1,-1),(1,-2)))
allTetrominos.append(((0,0),(0,1),(1,1),(2,1)))
allTetrominos.append(((0,0),(1,0),(0,1),(0,2)))
allTetrominos.append(((0,0),(1,0),(0,1),(1,1)))
allTetrominos.append(((0,0),(1,0),(2,0),(0,1)))
allTetrominos.append(((0,0),(1,0),(1,1),(1,2)))
allTetrominos.append(((0,0),(1,0),(2,0),(2,-1)))
allTetrominos.append(((0,0),(0,1),(0,2),(1,2)))
allTetrominos.append(((0,0),(1,0),(1,-1),(2,-1)))
allTetrominos.append(((0,0),(0,1),(1,1),(1,2)))
allTetrominos.append(((0,0),(1,0),(1,1),(2,1)))
allTetrominos.append(((0,0),(0,1),(1,0),(1,-1)))
allTetrominos.append(((0,0),(1,0),(1,-1),(2,0)))
allTetrominos.append(((0,0),(0,1),(0,2),(1,1)))
allTetrominos.append(((0,0),(1,0),(1,1),(2,0)))
allTetrominos.append(((0,0),(1,0),(1,-1),(1,1)))
patternsForPlacing = []
nextColumnComplete = []
finishedCount = 0


#a carpet class
class Carpet:
    
    #init
    def __init__(self, width, height):
        self.windowSize = 4
        self.maxX = height - 1
        self.maxY = width - 1
        self.width = width
        self.windowOffset = 0
        self.solutionCount = 1
        self.hashstore = 0
    # shift the window down
    def windowShift(self):
        self.windowOffset+=1
        self.hashstore = self.hashstore >> (self.width)
        
    # Makes a copy
    def copy(self):
        copy = Carpet(self.width, self.maxX+1)
        copy.windowOffset = self.windowOffset
        copy.solutionCount = self.solutionCount
        copy.hashstore = self.hashstore
        return copy

    # Tries to change a point in the carpet, if it fails returns False otherwise returns True
    def setSpot(self,x,y):
        if x < 0 or y < 0 or x+self.windowOffset > self.maxX or y > self.maxY:
            return False
        bit = 1 << ((x*(self.width))+y)
        if (bit & self.hashstore) == bit:
            return False
        self.hashstore += bit
        return True

    # Place a tile into this carpet
    def placeTile(self, tile, spot):
        ret = self.setSpot(spot[0]+tile[0][0], spot[1]+tile[0][1])
        ret = ret and self.setSpot(spot[0]+tile[1][0], spot[1]+tile[1][1])
        ret = ret and self.setSpot(spot[0]+tile[2][0], spot[1]+tile[2][1])
        ret = ret and self.setSpot(spot[0]+tile[3][0], spot[1]+tile[3][1])
        return ret
    
    # is the first column completed
    def isFirstColumnComplete(self):
        for y in range(self.width):
            if self.spotValue(0, y):
                return False
        return True
    
    # is the value at x,y empty
    def spotValue(self,x,y):
        bit = 1 << ((x*(self.width))+y)
        if (bit & self.hashstore) == bit:
            return False
        return True
    

    # What is the first empty spot
    def getFirstEmptySpot(self):        
        for x in range(self.windowSize):
            for y in range(self.width):
                if self.spotValue(x,y):
                    if(x+self.windowOffset<=self.maxX):
                        return (x,y)
        return None

    # Is self solved
    def isSolved(self):
        if self.windowOffset <= self.maxX - self.windowSize:
            return False        
        for x in range(self.windowSize+1):
            for y in range(self.width):
                if self.spotValue(x,y):
                    return x+self.windowOffset > self.maxX


    # equals override
    def __eq__(self,other):
        if other != None:
            if self.windowOffset == other.windowOffset and self.hashstore == other.hashstore:
                return True
        return False
    
    #less than override
    def __lt__(self, other):
        return self.hashstore < other.hashstore

# Places tiles
def TilePlacer():
    pattern = getNextPatternForTiling()
    global finishedCount
    while pattern != None:
        if pattern.isFirstColumnComplete():
            nextColumnComplete.append(pattern)
        else:
            p = pattern.getFirstEmptySpot()
            if p != None:
                for tile in allTetrominos:
                    copy = pattern.copy()
                    if copy.placeTile(tile, p):
                        if copy.isSolved():
                            finishedCount += copy.solutionCount
                        else:
                            patternsForPlacing.append(copy)
        pattern = getNextPatternForTiling()

# get the next carpet
def getNextPatternForTiling():
    global nextColumnComplete
    if len(patternsForPlacing) == 0 and len(nextColumnComplete) > 0:        
        nextColumnComplete.sort()
        i = 0
        while len(nextColumnComplete) > i:
            done = False
            pattern = nextColumnComplete[i]
            while not done:
                i += 1
                if i<len(nextColumnComplete):
                    if pattern == nextColumnComplete[i]:
                        pattern.solutionCount += nextColumnComplete[i].solutionCount
                    else:
                        done = True
                else:
                    done = True
            pattern.windowShift()
            patternsForPlacing.append(pattern)
        nextColumnComplete = []
    if len(patternsForPlacing) > 0:
        ret = patternsForPlacing[0]
        del patternsForPlacing[0]
        return ret
    return None

def SolveFor(width, height):
    global finishedCount
    patternsForPlacing.append(Carpet(width, height))
    TilePlacer()
    ret = finishedCount
    finishedCount = 0
    return ret

lines = stdin.readlines()

for line in lines:
    line = line.strip()
    regeer = "^(1|2|3|4|5|6) ((100)|([0-9][0-9]?))$"
    if re.fullmatch(regeer, line, flags=0):
        item = re.split(' ',line, flags=0)
        width = int(item[0])
        height = int(item[1])
        if((width*height)%4==0):
            print("%s %s" % (width, height))
            print("#%s"% SolveFor(width, height))
        else:
            print("%s %s" % (width, height))
            print("#0")
