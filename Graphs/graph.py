import pandas
import json
import vincent

dates_EFCvAFC = []
f=open("../Datasets/finalmufcvsmcfc.json")
# f is the file pointer to the JSON data set
i=0
for line in f:
	tweet = json.loads(line)
	i=i+1
	print i
	dates_EFCvAFC.append(tweet['created_at'])
	

# a list of "1" to count the hashtags
ones = [1]*len(dates_EFCvAFC)
# the index of the series
idx = pandas.DatetimeIndex(dates_EFCvAFC)
# the actual series (at series of 1s for the moment)
EFCvAFC = pandas.Series(ones, index=idx)

# Resampling / bucketing
# per_minute = EFCvAFC.resample('1Min').sum().fillna(0,inplace=True)
#print EFCvAFC.resample('1Min',how='sum')
time_chart = vincent.Line(EFCvAFC.resample('1Min',how='sum').fillna(0))
time_chart.legend(title='Man City vs Man United(no noise)') 
time_chart.axis_titles(x='Time Elapsed since start', y='Tweet Volume')
time_chart.to_json('time_chart2.json')

