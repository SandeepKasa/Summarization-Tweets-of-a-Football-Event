import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
	def on_data(self, data):
		try:
			with open('chelseavssouthampton.json', 'a') as f:
				f.write(data)
#			print data
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print(status)
		return True

auth = OAuthHandler("YLrWFnatmOhGzNIx5l1QMivZM","WL1GGvkVTkGAfxiJJi5BKR2nWJaM8h7vAQz0MBs1XHgXSddH1B")
auth.set_access_token("2553967664-TFYtwEIeaWsDnHZm4FHH8WTXYyo9V9hC3VJC2WS","eOdgYSPCfuJeHwjH3g1PrueaWIfOvEeXatZQBhGgGDZD6")
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#CFC or #SOUCHE or #CFCLive or #SaintsFC or #saintsfc'])
