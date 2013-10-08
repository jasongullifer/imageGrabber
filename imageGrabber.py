import urllib
import os
import Image
import xlrd
import csv

csvFile = csv.DictReader(open('testFillers.csv'))
pictureDir = './pictures/'
convertedDir = './pictures/converted/'
convertedFileType = 'png'
errorFile = open('errors.txt', 'w')

lines = list(csvFile)
numLines = len(lines)

if not os.path.exists(pictureDir):
    print 'Creating picture directory'
    os.makedirs(pictureDir)
    
if not os.path.exists(convertedDir):
    print 'Creating converted picture directory'
    os.makedirs(convertedDir)

lineNum = 1

for line in lines:
    flag=True
    print '\nWorking on line ' + str(lineNum) + ' of ' + str(numLines) + '.'
    fileName, fileType = os.path.splitext(line['ImageLink'])
    fileType = fileType.split('?')[0]

    originalFile = pictureDir + str(line['Item Number']) + '_' + line['Target Word'] + fileType
    convertedFile = convertedDir + str(line['Item Number']) + '_' + line['Target Word'] + '.' + convertedFileType

    if not os.path.isfile(convertedFile):
        try:
            urllib.urlretrieve(line['ImageLink'], originalFile)
            im = Image.open(originalFile)
        except IOError:
            flag=False
            print '    Can\'t retrieve image for item number ' + str(line['Item Number'])
            errorFile.write(str(line) + '\n')

        if flag:
            im.save(convertedFile)
            
    else:
        print '    File "' + os.path.split(convertedFile)[1]  + '" already exists. Skipping...'
    lineNum += 1
        
errorFile.close()
