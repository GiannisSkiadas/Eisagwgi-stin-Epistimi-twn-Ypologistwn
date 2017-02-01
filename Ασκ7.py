#!/usr/bin/env python
# -*- coding: utf_8 -*-

import tweepy
from tweepy import OAuthHandler
from twython import Twython 
import time


consumer_key = 'sdCbo0ShDgLFU5GTmBOqAF213'
consumer_secret = 'Rt1nmhraf7BeB8wpnRNgl5KTmFPfxMVf6cTREz9cD0CMcaa3iY'
access_token = '2211372450-tG13S0H1tOOYW07YUMIz7UY1ZIWV62vV5YVOqZp'
access_secret = 'LEi1zviGbZklRUeriBzNUnkNYpc8z6ZmvqIHYWD1S1PZg'



twitter = Twython(consumer_key,consumer_secret,access_token,access_secret)
id=[]
lis1=[]
lis2=[]
def counter(k):
	wordlist = k.split()
	i=0
	wordfreq = []
	for w in wordlist:
		wordfreq.append(wordlist.count(w))
		i+=1
	return i
	
def a(id):
	user_timeline = twitter.get_user_timeline(screen_name=id,count=10)
	time.sleep(1)
	return user_timeline

for i in range(1,3):
	b = raw_input("Dwse to tweeter id tou %sou xristi: @"%i)
	id.append(b)
	user_timeline=a(b)
	for tweet in user_timeline:
		p=tweet['text']+" "
		if (i==1):
			lis1.append(p)
			
		else:
			lis2.append(p)
		
k1="".join(lis1)	
k2="".join(lis2)
p=counter(k1)
d=counter(k2)
prwtos=len(k1)
deuteros=len(k2)


if (p>d):
	print "O @%s xristis exei perissoteres le3eis sta teleutaia 10 tweets tou." %id[0]
else:
	print "O @%s xristis exei perissoteres le3eis sta teleutaia 10 tweets tou." %id[1]
	
#ekana kai metriti grammatwn
if (prwtos>deuteros):
	print "O @%s xristis exei perissotera grammata sta teleutaia 10 tweets tou." %id[0]
else:
	print "O @%s xristis exei perissotera grammata sta teleutaia 10 tweets tou." %id[1]
