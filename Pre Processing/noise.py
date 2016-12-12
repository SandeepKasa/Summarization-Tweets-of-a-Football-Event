#!/usr/bin/python
import json
import os
def decode_json(line):
	try:
		return json.loads(line)
	except:
		return None

if __name__=='__main__':
	f=open('mufcvsmcfc.json','r')
	fw=open('limit.json','w')
	for lin in f:
		data=json.loads(lin)
		try:
			temp=data["created_at"]
			fw.write(lin)
		except:
			pass
	with open("limit.json") as fw:
	 	tweet = [decode_json(line) for line in fw]
	#print len(tweet)
	fw1=open('final.json','w')
	ban=[]
	for i in xrange(0,len(tweet)):
		d=tweet[i]["user"]["id"]
		if i in ban:
				continue
		count=0
		j=0
		for j in xrange(0,len(tweet)):
			e=tweet[j]["user"]["id"]
			if i!=j and e==d:
				count+=1
		if count>100 or count <2  :
			ban.append(i)
		else :
			fw1.write(json.dumps(tweet[i]))
			fw1.write('\n')
	with open("final.json") as fw1:
	 	tweet2 = [decode_json(line) for line in fw1]
	fw2=open('finalmufcvsmcfc.json','w')
	for i in xrange(0,len(tweet2)):
		t=tweet2[i]["text"]
		#print t
		if "Live Stream" in t:
			#print i
			continue
		else:
			fw2.write(json.dumps(tweet2[i]))
			fw2.write('\n')
	os.remove("limit.json")
	os.remove("final.json")

