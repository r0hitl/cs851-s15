'''
Created on Feb 8, 2015

@author: rlambi
'''
import subprocess
import os
import thread
import threading
import csv
import datetime

def fetchWebPage(url, fileName):
    print 'Fetching ', url
    #subprocess.Popen(["wget","-E","-H","-k","-K","-p", url])
    subprocess.Popen(["wget","--output-document=" + fileName, url]) # + ".html"
    
sites = 'sites'
if not os.path.exists(sites):
    os.makedirs(sites)

os.chdir(sites)

fieldNames = ['sno','seqNum','tcoUrl','url'] 

print datetime.datetime.now()
with open('../tweets-processed-1.txt') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=fieldNames, delimiter='\t')
    for row in reader:
        #fetchWebPage(row['url'])  
        thread.start_new_thread(fetchWebPage, (row['url'], row['sno'], ))

print datetime.datetime.now()

print 'Waiting for all threads to complete'
while threading.activeCount() > 1:
    print str(threading.activeCount())
    pass

print 'Completed fetching all webpages'
print datetime.datetime.now()


    
