# Some of the code used is from http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
from os import path
from collections import OrderedDict

def sort_by_value(item):
    return item[-1]

def removePunctuation(word):

    word = re.sub('[\",():;?\\[\\].{}#$&_*+=%!<>~0-9]', '', word)
    return word


def build_dict(filename, count):
    f = open(filename, 'rU')
    words = f.read().split()
    
    for word in words:
        word = word.lower()
        word = word.strip()
        
        word = removePunctuation(word);	
        
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    f.close()

    return count

def write_words(PATH, dict):
	
    files = [f for f in os.listdir(PATH) if path.isfile(path.join(PATH, f))]
    #print files
    
    for f in files:
        filename = PATH + f
        dict = build_dict(filename, dict)
       
    
    

def main():
    
    totalWords = 0
    totalUniqueWords = 0
    dict = {}
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/sites/'
    write_words(PATH, dict)
    
    odict = OrderedDict(sorted(dict.items(), key=lambda t: t[1]))
    
    fil = open('word-count.txt', 'w')
    odict.pop("\t", None)
    #for word in sorted(dict.keys()):
    for word in reversed(odict.keys()):
        
        freq = odict[word]
        
        if word is not None and freq is not None:    			
		if totalUniqueWords < 50000:
                	fil.write(word + '\t' + str(freq) + '\n')
		totalWords += freq
            	totalUniqueWords += 1
        
    fil.close()

    print 'Total Words\t', str(totalWords), '\n'
    print 'Total Unique Words\t', str(totalUniqueWords)
    sys.exit(1)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
