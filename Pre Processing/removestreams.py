import sys
import json
f=open(sys.argv[1],'r')
fw=open("mufcvsmcfc.json",'w')
for line in f:
	data=json.loads(line)
	t=data["text"].encode('utf-8').strip()
	t=t.replace("\n",' ')
	t=t.decode('unicode_escape').encode('ascii','ignore')
	if "stream" in t.lower().split():
		pass
	else:
	 	fw.write(line)

f.close()
fw.close()
