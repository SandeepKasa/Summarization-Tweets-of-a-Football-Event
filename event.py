import json
import datetime
from tfidf2 import *
list=[]
with open('./Graphs/time_chart.json') as data_file:    
    data = json.load(data_file)
time=[]
for i in range(len(data["data"][0]["values"])-1):
	if(data["data"][0]["values"][i+1]["val"]-data["data"][0]["values"][i]["val"]>=0):
		list.append(data["data"][0]["values"][i+1]["val"]-data["data"][0]["values"][i]["val"])
		time.append([data["data"][0]["values"][i+1]["val"]-data["data"][0]["values"][i]["val"],data["data"][0]["values"][i+1]["idx"]])
list.sort()
if len(list)%2 is 0:
	a=(len(list)+1)/2 - 1
	b=a+1
	med = (list[a] + list[b])/2
else:
	med=list[(len(list)+1)/2 - 1]

finlist=[]
#print " "
#print "VALUE OF THE THRESHOLD : " , 3*med
#print " ----- " 
for i in range(len(list)):
	if list[i]>=3*med:
		finlist.append(list[i])

fintime=[]
for i in range(len(finlist)):
	for j in range(len(time)):
		if finlist[i] is time[j][0]:
			fintime.append(time[j][1])
			time[j][1]=-1

final=[]
for i in range(len(fintime)):
	if fintime[i] != -1:
		final.append(fintime[i])

final.sort()
#print " "
#print "                         " + "Peak Time" + "   " + "Start Time" +  "  " + "End Time"
#print " "
for i in range(len(final)):
	final[i]=datetime.datetime.fromtimestamp(final[i]/1000.0)
	starttime = final[i] - datetime.timedelta(seconds=60)
	endtime   = final[i] + datetime.timedelta(seconds=60)
	if i/10 == 0 :
		print "Sub-event"+" "+"0"+str(i) + " - " , final[i] , " " , starttime.time() , " " , endtime.time()
	else:
		print "Sub-event"+" "+str(i) + " - " , final[i] , " " , starttime.time() , " " , endtime.time()

eventtweets=[]
links=[]
cnt=[]
ftweets = open("./Datasets/finalmufcvsmcfc.json",'r')
for ind in xrange(0,len(final)):
	cnt=[]
	fw = open("temp.json",'w')
	starttime = final[ind] - datetime.timedelta(seconds=60)
	endtime   = final[ind] + datetime.timedelta(seconds=60)
        ftweets = open("./Datasets/finalmufcvsmcfc.json",'r')
	for line in ftweets:
		text = json.loads(line)
		tiimme=text["created_at"].split()[3]
		tobecmp=datetime.datetime.strptime(tiimme,'%H:%M:%S').time()
		if(tobecmp>=starttime.time() and tobecmp<=endtime.time()):
			fw.write(line)
	
	findbest("temp.json")
	ff = open("out.txt",'r')
	fe = open("url.txt",'r')
	k=1
	for line in ff:
		if line in eventtweets:
			cnt.append(k)
			pass
		else:
			eventtweets.append(line)
		k=k+1
	k=1
	for line in fe:
		if line in links:
			pass
		elif k in cnt:
			pass
		else:
			links.append(line)
		k=k+1

#	break
	ff.close()
	fe.close()
fp = open("out.txt",'w')
fs = open("url.txt",'w')
for i in eventtweets:
	fp.write(i)
#	fd.write("\n")
for i in links:
	fs.write(i)
fp.close()
fs.close()
