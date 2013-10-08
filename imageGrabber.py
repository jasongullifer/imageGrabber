import urllib
import os
import Image
import xlrd
import csv

csvFile = csv.DictReader(open('testFillers.csv'))
pictureDir = './pictures/'
convertedDir = './pictures/converted/'
errorFile = open('errors.txt', 'w')

lines = list(csvFile)
numLines = len(lines)

if not os.path.exists(pictureDir):
    os.makedirs(pictureDir)
    
if not os.path.exists(convertedDir):
    os.makedirs(convertedDir)

lineNum = 1
for line in lines: 
    print 'Working on line ' + str(lineNum) + ' of ' + str(numLines) + '.'
    fileName, fileType = os.path.splitext(line['ImageLink'])
    fileType = fileType.split('?')[0]
    try:
        urllib.urlretrieve(line['ImageLink'], pictureDir + str(line['Item Number']) + '_' + line['Target Word'] + fileType)
        im = Image.open(pictureDir + str(line['Item Number']) + '_' + line['Target Word'] + fileType)
        im.save(convertedDir + str(line['Item Number']) + '_' + line['Target Word'] + '.png')
    except IOError:
        print 'Can\'t open image for item number ' + str(line['Item Number'])
        errorFile.write(str(line) + '\n')
    lineNum += 1
        
errorFile.close()
