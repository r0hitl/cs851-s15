# Some of the code used is from http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
from os import path

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
    
    dict = {}
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/1/'
    write_words(PATH, dict)
    
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/2/'
    write_words(PATH, dict)
   
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/3/'
    write_words(PATH, dict)
    
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/4/'
    write_words(PATH, dict)
    
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/5/'
    write_words(PATH, dict)
    
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/6/'
    write_words(PATH, dict)
    
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/7/'
    write_words(PATH, dict)
    
    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/8/'
    write_words(PATH, dict)

    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/9/'
    write_words(PATH, dict)

    PATH = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/A3/boilerpipe_text/10/'
    write_words(PATH, dict)

    fil = open('word-count-boilerpipe.txt', 'w')    
    dict.pop("\t", None)
    totalWords = 0
    totalUniqueWords = 0
    for word in sorted(dict.keys()):
        
        freq = dict[word]
        
        if word is not None and freq is not None: 			
			fil.write(word + '\t' + str(dict[word]) + '\n')
			totalWords += freq
			totalUniqueWords += 1
        
    fil.close()

    print 'Total Words\t', str(totalWords), '\n'
    print 'Total Unique Words\t', str(totalUniqueWords)

    sys.exit(1)

if __name__ == '__main__':
    main()
