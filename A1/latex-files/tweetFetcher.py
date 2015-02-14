'''
Created on Jan 31, 2015

@author: rlambi
'''
import tweepy
import time
import json
from datetime import datetime

CONSUMER_KEY = "iuKUndPfIF5aWnNl0Ayq9Ztgt"
CONSUMER_SECRET = "QuNsF4gL2LssmbcdtKpyLZGiQctz98T4hXWcAKrBYGh72ZTFC8"

OAUTH_TOKEN = "549294315-P89swbZzgiP2n9bq6fW2T2jm5etru6Wr6TN08Lg3"
OAUTH_TOKEN_SECRET = "NMzDaS5doFtHxXxebE68AunmRHTsFfLxwAkk3LsDN75JH"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

fil = open('tweets.txt', 'w')
log = open('log.txt', 'w')
data = {}
url_list = []
urls = []

seqNum = 0
log.write('Start: ' + str(0) + datetime.now().time().__str__() + '\n')

myCursor = tweepy.Cursor(api.search, q="http:links", rpp=100).items()

while True:    
    try:
        tweet = myCursor.next()

        url_list = tweet._json['entities']['urls']

        urls[:] = []
        if url_list.__len__() > 0:
            seqNum += 1
            
            print seqNum, " ", url_list
            
            for url in url_list:
                urls.append(url['url'])
                
            data['id_str'] = tweet._json['id_str']
            data['text'] = tweet._json['text']
            data['created_at'] = tweet._json['created_at']
            data['urls'] = urls
            data['seqNum'] = seqNum
            
            json_tweet = json.dumps(data)            
            fil.write(json_tweet + '\n')
    except tweepy.TweepError:
        
        tmp = 'Sleep at ' + str(seqNum) + ' ' + datetime.now().time().__str__()  + '\n'        
        print tmp
        log.write(tmp)
        time.sleep(900)
        
        tmp = 'Wakeup: ' + datetime.now().time().__str__() + '\n'
        print tmp
        log.write(tmp)
        continue
    
    if seqNum == 10000:
        break


print "Total tweets: ", seqNum
log.write('Stop: ' + datetime.now().time().__str__() + '\n')
log.write("Total tweets: " + str(seqNum))

log.close()
fil.close()

