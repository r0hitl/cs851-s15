'''
Created on Feb 5, 2015

@author: rlambi
'''
import requests
import requests.exceptions
import json
import csv
import os

filePath = '/home/rlambi/rohit/Courses/Digital-Libraries/Assignments/'
outputDir = filePath + 'output_2/'  

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

finalURIs = []
duplicateUrlsCount = 0
uniqueUrlsCount = 0
skippedUrlsCount = 0
serialNo = 1
fileTweets = open(filePath + 'tweets.txt', 'r')
fileHttpStatuses = open(outputDir + 'http-statuses.txt', 'w')
fileUrls = open(outputDir + 'tweets-processed-1.txt', 'w')
skippedUrls = open(outputDir + 'skippedUrls.txt', 'w')

httpStatusMap = {}
redirectsMap = {}

xx = 1
for line in fileTweets:
    
#     print line
    tweet = json.loads(line)
#     print tweet
    tweetedOn = tweet['created_at'] 
    urlList = tweet['urls']
    
    for url in urlList:
        
        resp = requests.Response()
        try:
            resp = requests.head(url, allow_redirects=True, timeout=10)
            
#             print resp
#             print resp.status_code
#             print resp.history
            redirectCount = len(resp.history)
            terminalURI = resp.url
            print serialNo, '\t', tweet['seqNum'], '\t' + url + '\t' + terminalURI + '\t' + tweetedOn + '\t' + str(redirectCount)
            fileUrls.write(str(serialNo) + '\t' + str(tweet['seqNum']) + '\t' + url + '\t' + terminalURI + '\t' + tweetedOn + '\t' + str(redirectCount) + '\n')
            resp.history.append(resp)
#             print resp.history
            
            # Check in HttpStatusMap if this statusCode is already present and add/update its count accordingly 
            for respHist in resp.history:
                fileHttpStatuses.write(str(respHist.status_code) + '\n')
            
            
#             if redirectCount in redirectsMap:
#                 redirectsMap[redirectCount] = redirectsMap[redirectCount] + 1
#             else:
#                 redirectsMap[redirectCount] = 1
            
            
            if finalURIs.count(terminalURI) == 0:
                finalURIs.append(terminalURI)
            else:
                duplicateUrlsCount += 1
            
            serialNo += 1
            
        except requests.exceptions.Timeout:
            print 'Timeout ' + str(tweet['seqNum']) + '\t' + url
            skippedUrls.write(str(tweet['seqNum']) + '\t' + url)
            skippedUrlsCount += 1
        except:
            print 'Skipped ' + str(tweet['seqNum']) + '\t' + url
            skippedUrls.write('Skipped ' + str(tweet['seqNum']) + '\t' + url)
            skippedUrlsCount += 1 
        
#     if xx == 50:
#         break
#     xx += 1



uniqueUrlsCount = len(finalURIs)
print 'uniqueUrls: ', uniqueUrlsCount
print 'duplicateUrls: ', duplicateUrlsCount
print 'skippedUrls: ', skippedUrlsCount
print httpStatusMap
print redirectsMap

fileUrlCount = open(filePath + 'url-count.txt', 'w')
fileUrlCount.write('uniqueUrls:', '\t', str(uniqueUrlsCount))
fileUrlCount.write('duplicateUrls:', '\t', str(duplicateUrlsCount))
fileUrlCount.close()

skippedUrls.close()
fileUrls.close()
fileTweets.close()
fileHttpStatuses.close()
