import os
import thread
import threading
import csv
import datetime
from boilerpipe.extract import Extractor



iteration = '10'
BOILERPIPE_TEXT = 'boilerpipe_text/' + iteration
if not os.path.exists(BOILERPIPE_TEXT):
    print 'Creating folder - ' + BOILERPIPE_TEXT
    os.makedirs(BOILERPIPE_TEXT)


def fetchWebPage(URL):
    
    extractor = Extractor(url=URL)
    extracted_text = extractor.getText()
    return extracted_text


fieldNames = ['sno','seqNum','tcoUrl','url'] 

print datetime.datetime.now()

totalUrls = 0
skipCnt = 0
emptyContent = 0

skipped = open("skipped-" + iteration + ".txt", 'w')
with open(iteration + '.txt') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=fieldNames, delimiter='\t')
    
    for row in reader:   
		     
        totalUrls += 1
        try:
            print 'Fetching ', str(row['sno']), ' ', row['url']
            extracted_text = fetchWebPage(row['url'])
            
            if not extracted_text:
				emptyContent += 1
            
            fil = open(BOILERPIPE_TEXT + '/' + row['sno'], 'w')
            fil.write(extracted_text.encode('UTF-8'))
            fil.close()
            
        except:
			skipCnt += 1
			skipped.write(row['sno'] + '\t' + row['url'] + '\n')
			
skipped.close()		
	
print datetime.datetime.now()

summary = open("summary-" + iteration + ".txt", 'w')
summary.write("TotalUrls - " + str(totalUrls))
summary.write("\nSkipped - " + str(skipCnt))
summary.write("\nEmpty Content - " + str(emptyContent))
summary.close()

print 'Completed fetching all webpages'
print datetime.datetime.now()

