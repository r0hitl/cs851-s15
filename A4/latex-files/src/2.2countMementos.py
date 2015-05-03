import json
import os

INPUT_PATH = '2.timemaps/'
OUTPUT_PATH = 'mementoCount/'
OUTPUT_FILE = 'mementoCount.txt'

if not os.path.exists(OUTPUT_PATH):
    print 'Creating folder - ' + OUTPUT_PATH
    os.makedirs(OUTPUT_PATH)

fileList = os.listdir(INPUT_PATH)
#fileList = ['1201']
oFile = open(OUTPUT_PATH + OUTPUT_FILE, 'w')
for fName in fileList:
    f = open(INPUT_PATH + fName, 'r')
    jsonContent = f.read()
    
    if len(jsonContent) == 0:
        mementoCount = 0
    else:
        fContent = json.loads(jsonContent)
        #print fContent['mementos']['list'][0]['uri']
        try:
            mementoCount = len(fContent['mementos']['list'])
        except KeyError:
            mementoCount = 0
            
    oFile.write(fName + '\t' + str(mementoCount) + '\n')
    f.close()

oFile.close()