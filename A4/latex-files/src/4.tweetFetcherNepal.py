'''
@author: rlambi
'''
import os
import json
from twarc import Twarc

CONSUMER_KEY = "iuKUndPfIF5aWnNl0Ayq9Ztgt"
CONSUMER_SECRET = "QuNsF4gL2LssmbcdtKpyLZGiQctz98T4hXWcAKrBYGh72ZTFC8"

OAUTH_TOKEN = "549294315-P89swbZzgiP2n9bq6fW2T2jm5etru6Wr6TN08Lg3"
OAUTH_TOKEN_SECRET = "NMzDaS5doFtHxXxebE68AunmRHTsFfLxwAkk3LsDN75JH"

'''
os.system('python twarc/twarc.py --consumer_key iuKUndPfIF5aWnNl0Ayq9Ztgt --consumer_secret QuNsF4gL2LssmbcdtKpyLZGiQctz98T4hXWcAKrBYGh72ZTFC8 --access_token 549294315-P89swbZzgiP2n9bq6fW2T2jm5etru6Wr6TN08Lg3 --access_token_secret NMzDaS5doFtHxXxebE68AunmRHTsFfLxwAkk3LsDN75JH --search "statue of liberty bomb" > tweets1.json')
'''

t = Twarc(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

fil = open('tweets_nepal_5.txt', 'w')
counter = 0
for tweet in t.search("nepal earthquake"):
    counter += 1        
    json_tweet = json.dumps(tweet)            
    print(json_tweet + '\n')
    fil.write(json_tweet + '\n')
    
    if counter == 1000:
		break

fil.close()

print 'End'




