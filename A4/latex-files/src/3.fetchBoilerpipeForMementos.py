import json
import os
from boilerpipe.extract import Extractor
from nltk.util import ngrams
import urllib2

INPUT_PATH = '3.selected-timemaps/'
OUTPUT_PATH = 'mementos/'
OUTPUT_FILE = 'mementoCount.txt'

def removePunctuation(paragraph):

    paragraph = re.sub('[\",():;?\\[\\].{}#$&_*+=%!<>~0-9]', '', paragraph)
    return paragraph


def normalizeString(paragraph):
   
    words = paragraph.split()
    normalizedWordList = []
    
    for word in words:
        word = word.lower()
        word = word.strip()
        
        #word = removePunctuation(word);	
        normalizedWordList.append(word)
        
    return normalizedWordList

def getUniqueNgram(paragraph, n):
	nGrams = ngrams(normalizeString(paragraph), n)
	uniqueNGrams = set(nGrams)
	return uniqueNGrams

def calculateJaccardDistance(a3Words, a4Words):
    union = set(a3Words).union(a4Words)
    intersect = set(a3Words).intersection(a4Words)
    jacDist = (len(union) - len(intersect)) * 1.0 / len(union)
    return jacDist

def getNgrams(filePath):
    f = open(filePath, 'r')
    paragraph = f.read()
    f.close()
    uniGram = getUniqueNgram(paragraph, 1)
    return uniGram

def saveBoilerpipeText(URL, mementoId, bPipeOpFilePath):
    extractor = Extractor(url=URL)
    extracted_text = extractor.getText()
    
    fil = open(bPipeOpFilePath, 'w')
    fil.write(extracted_text.encode('UTF-8'))
    fil.close()
    


if not os.path.exists(OUTPUT_PATH):
    print 'Creating folder - ' + OUTPUT_PATH
    os.makedirs(OUTPUT_PATH)

fileList = os.listdir(INPUT_PATH)
#fileList = ['1201']


for fName in fileList:
    print 'processing for ' + fName
    iFile = open(INPUT_PATH + fName, 'r')
    jsonContent = iFile.read()
    
    if len(jsonContent) != 0:        
        fContent = json.loads(jsonContent)
        #print fContent['mementos']['list'][0]['uri']
        mementoURIs = fContent['mementos']['list']
        BPIPE_OUTPUT_PATH = OUTPUT_PATH + fName + '/'
        
        if not os.path.exists(BPIPE_OUTPUT_PATH):
            os.makedirs(BPIPE_OUTPUT_PATH)
        
        oFile = open(BPIPE_OUTPUT_PATH + 'jacard-distance.txt', 'w')
        for i, URI in enumerate(mementoURIs):
            mementoId = i + 1
            bPipeOpFilePath = BPIPE_OUTPUT_PATH + str(mementoId)            
            
            try:
                print str(mementoId), '\t', URI['uri']
                saveBoilerpipeText(URI['uri'], mementoId, bPipeOpFilePath)                
                currentMementoWords = getNgrams(bPipeOpFilePath)
                
                if mementoId == 1:
                    firstMementoWords = currentMementoWords                
                
                if currentMementoWords != None:
                        jacDist = calculateJaccardDistance(firstMementoWords, currentMementoWords)                        
                        oFile.write('1\t' + str(mementoId) + '\t' + str(jacDist) + '\t' + URI['datetime'] +  '\n')
            except urllib2.HTTPError:
                print 'HTTP Error'
                continue
            except:
                print 'Error'
                continue
                
        oFile.close()   
    
    iFile.close()   

