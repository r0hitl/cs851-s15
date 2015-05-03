import os
from nltk.util import ngrams
import re


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
	
def getNgrams(filePath):
	f = open(filePath, 'r')		
	paragraph = f.read()
	f.close()
	
	uniGram = getUniqueNgram(paragraph, 1)
	biGrams = getUniqueNgram(paragraph, 2)		
	triGrams = getUniqueNgram(paragraph, 3)		

	grams = {'uniGram': uniGram, 'biGrams': biGrams, 'triGrams': triGrams}
	
	return grams


def writeNgrams(grams, oneGFile, twoGFile, threeGFile):
	oneGFile.write('\t' + str(len(grams['uniGram'])))
	twoGFile.write('\t' + str(len(grams['biGrams'])))
	threeGFile.write('\t' + str(len(grams['triGrams'])))

def writeJaccardDistance_old(a3Grams, a4Grams, oneGFile, twoGFile, threeGFile):
    oneGJD = str(calculateJaccardDistance(a3Grams['uniGram'], a4Grams['uniGram']))
    twoGJD = str(calculateJaccardDistance(a3Grams['biGrams'], a4Grams['biGrams']))
    threeGJD = str(calculateJaccardDistance(a3Grams['triGrams'], a4Grams['triGrams']))
    
    oneGFile.write('\t' + oneGJD + '\t' + twoGJD + '\t' + threeGJD)    
    
def writeJaccardDistance(a3Grams, a4Grams, fName, jdFile):
    oneGJD = str(calculateJaccardDistance(a3Grams['uniGram'], a4Grams['uniGram']))
    twoGJD = str(calculateJaccardDistance(a3Grams['biGrams'], a4Grams['biGrams']))
    threeGJD = str(calculateJaccardDistance(a3Grams['triGrams'], a4Grams['triGrams']))    
    jdFile.write(str(fName) + '\t' + oneGJD + '\t' + twoGJD + '\t' + threeGJD + '\n')
   

def calculateJaccardDistance(a3Words, a4Words):
    union = set(a3Words).union(a4Words)
    intersect = set(a3Words).intersection(a4Words)
    jacDist = (len(union) - len(intersect)) * 1.0 / len(union)
    return jacDist


A3_INPUT_PATH = '../A3/boilerpipe_text/all'
A4_INPUT_PATH = 'boilerpipe_text/all'

#A3_INPUT_PATH = '../A3/sample-boilerpipe/'
#A4_INPUT_PATH = 'sample-boilerpipe/'

A3Files = os.listdir(A3_INPUT_PATH)
A4Files = os.listdir(A4_INPUT_PATH)

OUTPUT_DIR = 'grams'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

oneGFile = open(OUTPUT_DIR + "/jaccard-distance.txt", 'w')

for fName in A3Files:
	if fName in A4Files:				
		a3fPath = A3_INPUT_PATH + '/' + fName
		a4fPath = A4_INPUT_PATH + '/' + fName
				
		a3Grams = getNgrams(a3fPath)
		a4Grams = getNgrams(a4fPath)

		if len(a3Grams['triGrams']) != 0 and len(a4Grams['triGrams']) != 0:
			writeJaccardDistance(a3Grams, a4Grams, fName, oneGFile)

		

oneGFile.close()
