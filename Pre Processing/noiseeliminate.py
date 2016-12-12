#!/usr/bin/python
import json
import sys
if __name__=='__main__':
	f=open(sys.argv[1],'r')
	fw=open(sys.argv[2],'w')
	for line in f:
		data=json.loads(line)
		try:
			temp=data["created_at"]
			fw.write(line)
		except:
			pass



