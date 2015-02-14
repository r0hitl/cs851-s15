'''
Created on Feb 7, 2015

@author: rlambi
'''
import requests
import json
import csv
import os
import datetime


def skip(row):
    print 'Skipped ' + '\t' + row['serialNo']  + '\t' + row['tweetSeqNo'] + '\t' + row['tcoURL'] + '\t' +  row['finalURL'] + '\t' +  row['tweetedOn'] + '\n' 
    errorLogFile.write('Skipped ' + '\t' + row['serialNo']  + '\t' + row['tweetSeqNo'] + '\t' + row['tcoURL'] + '\t' +  row['finalURL'] + '\t' +  row['tweetedOn'] + '\n')

serverURL = 'http://localhost:8080/cd?url='

tweetAgeMap = {}
filePath = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/'
inputFilePath = filePath + 'output_2/tweets-processed-1.txt'
outputDir = filePath + 'output_3/'  
outputFilePath = outputDir + 'url-dates.csv'
xx = 1
errorLogFile = open(outputDir + 'errorLog.txt', 'w')

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

with open(inputFilePath) as inputFile:
        reader = csv.DictReader(inputFile, delimiter='\t', fieldnames=['serialNo', 'tweetSeqNo', 'tcoURL', 'finalURL', 'tweetedOn', 'redirectCount'])
        
        with open(outputFilePath, 'wb') as outputFile:
            writer = csv.writer(outputFile, delimiter='\t')        
    
            try:
                for row in reader:
                    print 'Processing ', row['serialNo'], row['finalURL']
                    resp = requests.get(serverURL + row['finalURL'])
                    print resp.status_code
                    
                    if(resp.status_code == 200):
                        jsonResponse = json.loads(resp.text)                
                        
                        creationDate = datetime.datetime.strptime(jsonResponse['Estimated Creation Date'], '%Y-%m-%dT%H:%M:%S') # 2006-02-22T00:00:00  "%Y-%m-%d"
                        tweetedDate = datetime.datetime.strptime(row['tweetedOn'], "%a %b %d %H:%M:%S +0000 %Y") # Tue Feb 03 08:16:18 +0000 2015
                        
                        age = abs((creationDate.date() - tweetedDate.date()).days)                
                                        
                        writer.writerow([row['serialNo'], row['tweetSeqNo'], row['tcoURL'], row['finalURL'], row['tweetedOn'], jsonResponse['Estimated Creation Date'], age])
                        
                        if xx == 5:
                            break
                        xx += 1
                    else:
                        skip(row)
                    
                    
            except requests.exceptions.ConnectionError:
                print 'Cannot connect to server. Make sure server is running'
            except:    
                print 'Exception'            
                skip(row)
        

errorLogFile.close()
