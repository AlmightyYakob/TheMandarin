#! /usr/bin/env python

import math

from pip._vendor.requests.packages.urllib3.connectionpool import xrange
import tweepy, time, sys
from tweepy.models import Status


                                    #enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'prjiNXa8WHL5IOS4HNdnqxQRL'        #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'hHQ2OJeI26tpHhooihfBvwZ6jNXrlME3DCOKsoaFPKHnaHVhZt'     #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '837807691414274051-WMs9arq1V4SHo4mXWgG6YLaDhNbyyKM'          #keep the quotes, replace this with your access token
ACCESS_SECRET = 'Cm8aWMQSQVEtlzR8nEXYEBZl2vtS6O4mj0dXdz0yQNyzV'          #keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if (len(sys.argv) > 1):
    argfile = str(sys.argv[1])
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()
    
    
def is_prime(a):
    if (a<2): return False
    if (a%2 == 0): return False
    if(a==2): return True
    
    for i in range(3, int(math.sqrt(a)), 2):
        if (a%i == 0):
            return False
        
    return True


    

def tweet_prime_unix():
    while(True):
        timestamp = int(time.time())
        if (is_prime(timestamp)):
            print("PRIME FOUND: TWEET POSTED")
            status = ("The current UNIX timestamp (" + str(timestamp) + ") is a prime number!")
            api.update_status(status)
        else:
            print("No File Given")
        
        if (int(time.time()) == timestamp):
            time.sleep(1)
    



suggested = api.suggested_users


while(True):
    for i in suggested:
        id = suggested[i]   
    
        api.create_friendship(id)
    
    time.sleep(900)

