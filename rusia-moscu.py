'''

 
RUSIA - MOSCÚ
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "B8fbK6lq4aDTGrUcWYeol3bzG"
csecret = "mcmJUdrIfqt4ytSM9SLjy8hpkJLHbRZ1oyqqto6GWd09kdUMDu"
atoken = "862234674-3JN0dVtwRHCPD7jvJHkerjGIEg9oh8hcOhh1E6tv"
asecret = "LagAq8jH5DQurSHhsgb9TivGrCugiUH9Vr8jONlgoL1cg"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

 
URL = 'localhost'
db_name = 'rusia2'
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://192.168.100.134:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
 
 twitterStream.filter(locations=[31.6,55.5,93.9,67.6])  #RUSIA - MOSCÚ
