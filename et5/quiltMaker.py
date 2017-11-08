''' Cosc326 Levi Faid 3894507 Python 3.6.2 '''

from sys import stdin
import re

ourFile = open("YGQA(A-M)-Quilt-Design.html","w+")
ourFile.write("<!DOCTYPE html>\n<html>\n<body>\n")
lines = stdin.readlines()
boxes = []
for line in lines:
    line.strip()
    if(not re.search('^#', line, flags=0)):
        if(re.search('^((([0-9])+)|(([0-9])+.([0-9])+)) ([0-9])+ ([0-9])+ ([0-9])+', line, flags=0)):
            values = re.split(' ', line, flags=0)
            values[0] = float(values[0]);
            values[1] = int(values[1]);
            values[2] = int(values[2]);
            values[3] = int(values[3]);
            if values[1]<= 255 and values[2] <= 255 and values[3] <= 255:
                boxes.append([values[0],"rgb(%s,%s,%s)"% (values[1], values[2], values[3])])

if(len(boxes)!=0):    
    totalScaleValue = 0.0
    for line in boxes:
        totalScaleValue += line[0]
    while totalScaleValue<2.0:
        totalScaleValue = totalScaleValue*10
        for line in boxes:
            line[0] = line[0]*10

    ScaleToPixelSize = 800.0/totalScaleValue
    def makeBox(centerX, centerY, scale, colour, nextBoxes, zValue, Ssize):
        size = scale*Ssize
        x1 = centerX-(size/2)
        y1 = centerY-(size/2)
        x2 = x1+(size)
        y2 = y1+(size)
        ourFile.write("<div style = \"width:%spx;height:%spx;rgba(0, 0, 0, .2);background:%s;position:absolute;left:%spx;top:%spx;z-index:%s;\"></div>" % (size, size, colour, x1, y1, zValue))
        leftOver = list()
        if len(nextBoxes)>1:
            leftOver = nextBoxes[1:]
        if len(nextBoxes)!=0:        
            nextColour = nextBoxes[0][1]
            z = zValue+1;
            nextSize = int(nextBoxes[0][0])
            makeBox(x1, y1, nextSize, nextColour, leftOver, z, Ssize)
            makeBox(x1, y2, nextSize, nextColour, leftOver, z, Ssize)
            makeBox(x2, y1, nextSize, nextColour, leftOver, z, Ssize)
            makeBox(x2, y2, nextSize, nextColour, leftOver, z, Ssize)


    centerx = 400
    centery = 400
    if(len(boxes)>1):
        makeBox(centerx, centery, int(boxes[0][0]), boxes[0][1], boxes[1:], 0, ScaleToPixelSize)
    else:
        makeBox(centerx, centery, int(boxes[0][0]), boxes[0][1], list(), 0, ScaleToPixelSize)
ourFile.write("</body>\n</html>")
ourFile.close()






        
