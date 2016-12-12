import json
import re
value={"lead":1000,"goal":1000,"assist":700,"card":800,"score": 1000,"sub" : 400,"substitute":400,"subs":400,"red": 600,"yellow" : 500,"save": 300,"offside":100,"penalty":800,"corner":500,"free":500,"kick":500,"half":700,"time":700}
file = open('./Datasets/finalmufcvsmcfc.json', 'r')
dic={}
for line in file:
    data=json.loads(line)
    temp=data["text"]
    for i in temp.split():
		i=i.lower()
		regex = re.compile('[^a-z0-9]')
		i=regex.sub('', i)
    		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1


import operator
sorted_x = sorted(dic.items(), key=operator.itemgetter(1))
from nltk.corpus import stopwords
ans=[]
for i in sorted_x:
    if '#' not in i[0]:
        if 'http' not in i[0]:
            if i[0] not in stopwords.words('english'):
    			if ''!=i[0] and 'rt'!=i[0]:
    				ans.append((i[0],i[1]))

file = open('out.txt', 'r')
final=[]
count=0
cnt=0
for line in file:
    for i in line.split():
        i=i.lower()
        regex = re.compile('[^a-z0-9]')
        i=regex.sub('', i)
        if i in value:
            #print i,value[i],cnt
            count=count+value[i]
        for j in ans:
            if i==j[0]:
                count=count+j[1]
    final.append([cnt,count])
    count=0
    cnt+=1

for i in final:
    for j in final:
        if i[1]>j[1]:
            temp=i[0]
            i[0]=j[0]
            j[0]=temp
            temp=i[1]
            i[1]=j[1]
            j[1]=temp


import linecache
for j in final:
    print linecache.getline('url.txt', j[0]+1)








