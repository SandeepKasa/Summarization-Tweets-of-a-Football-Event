import re, math
from collections import Counter
import sys,json

WORD = re.compile(r'\w+')
base = "https://twitter.com/"
#myre = re.compile(u'['u'\U0001F300-\U0001F64F'u'\U0001F680-\U0001F6FF'u'\u2600-\u26FF\u2700-\u27BF]+',re.UNICODE)
stopwords =["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"];
idf={}
def get_cosine(vec1, vec2):
	intersection = set(vec1.keys()) & set(vec2.keys())
	numerator = sum([vec1[x] * vec2[x] for x in intersection])
	sum1 = sum([vec1[x]**2 for x in vec1.keys()])
	sum2 = sum([vec2[x]**2 for x in vec2.keys()])
	denominator = math.sqrt(sum1) * math.sqrt(sum2)
	if not denominator:
		return 0.0
	else:
		return float(numerator) / denominator

def find_idf(tweets,leng):
	for i in xrange(0,leng):
		words=WORD.findall(tweets[i].lower())
		words=[terms for terms in words if terms not in stopwords]
		for term in words:
			try:
				idf[term]=idf[term]+1
			except:
				idf[term]=1


def text_to_vector(text,leng):
	words = WORD.findall(text)
	words=[terms for terms in words if terms not in stopwords]

	#print dir(Counter(words))
	b=Counter(words)
	for key in b:
		b[key]=1+math.log(b[key],10)
		#print idf[key]
		b[key]=b[key]*(math.log(leng*1.0/idf[key],10))
	return b

def findbest(filename):
	tfidf={}
	tweets=[]
	temp=[]
	urls=[]
	f=open(filename,'r')
	#fw=open("output.txt",'w')
	k=0
	for line in f:
		try:
			data=json.loads(line)
			identifier = data["id"]
			screenname = data["user"]["screen_name"]
			tweet=data["text"].encode('utf-8').strip()
			tweet=tweet.replace("\n",' ')
			tweet=tweet.decode('unicode_escape').encode('ascii','ignore')
			if "stream" in tweet.lower().split(" "):
				pass
			else:
				if tweet in tweets:
					pass
				else:
					querywords = tweet.split()
					resultwords  = [word for word in querywords if '#' not in word]
					if not resultwords:
						pass
					else:
						resultwords  = [word for word in resultwords if not word.isdigit()]			
						if not resultwords:
							pass
						else:
							tweets.append(str(tweet))
							urls.append(str(base+str(screenname)+"/status/"+str(identifier)))
		except:
			pass
#		print urls
	leng = 20
    	find_idf(tweets,leng)
	for i in xrange(0,leng):
		summ=0
		#print i
		vector1 = text_to_vector(tweets[i].lower(),leng)
		for j in xrange(0,leng):
			if i!=j:
				#print j
				#print tweets[j]
				vector2 = text_to_vector(tweets[j].lower(),leng)
				cosine=get_cosine(vector1,vector2)
				summ=summ+cosine
		tfidf[i]=summ
	sortedtfidf=sorted(tfidf.values())
#	print "The Score of each tweet\n"
#	print sortedtfidf
#	print "\n"
	sortedtfidf=sortedtfidf[::-1]

	k=0
	fk = open("out.txt",'w')
	fg = open("url.txt",'w')
	for i in xrange(0,10):
	#	if(i>=len(tweets)):
	#		break
		ind=tfidf.keys()[tfidf.values().index(sortedtfidf[i])]
		k=k+1
		fk.write(tweets[ind])
		fk.write("\n")
		fg.write(urls[ind])
		fg.write("\n")

		
	fk.close()
	fg.close()

