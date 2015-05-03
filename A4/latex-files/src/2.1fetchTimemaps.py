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

def fetchTimemap(url, fileName):    
    url = "http://labs.mementoweb.org/timemap/json/" + url
    print "\n", str(fileName), url  
    #subprocess.Popen(["wget","--output-document=" + fileName, url]) # + ".html"
    command = "wget --output-document=" + fileName + " " + url
    print command
    os.system(command)
    
sites = 'timemaps'
if not os.path.exists(sites):
    os.makedirs(sites)

os.chdir(sites)

fieldNames = ['sno','seqNum','tcoUrl','url'] 

print datetime.datetime.now()
with open('../input-urls/10.txt') as csvfile:
#with open('../all-urls.txt') as csvfile:
#with open('../sample-urls.txt') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=fieldNames, delimiter='\t')
    for row in reader:
        fetchTimemap(row['url'], row['sno'])  
        #thread.start_new_thread(fetchWebPage, (row['url'], row['sno'], ))

print datetime.datetime.now()

#print 'Waiting for all threads to complete'
#while threading.activeCount() > 1:
 #   print str(threading.activeCount())
  #  pass

print 'Completed fetching all webpages'
print datetime.datetime.now()


    
