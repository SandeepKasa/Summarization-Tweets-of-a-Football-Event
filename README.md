# Summarization-Tweets-of-a-Football-Event
Goal : To summarize a football match selecting only those tweets that signify interesting occurences in the match.

-> Identified a significant need of the problem, and understood it as fully as possible in the context in which it occurs. 
-> Collected the tweets for three to four football matches by using the streaming API of twitter with the help of hash-tags.
-> Noise elimination is done on the streamed datasets to remove the irrelevant tweets.	
-> Absolute number of tweets on every streamed dataset(with noise and without noise) is plotted over the duration of the match.
-> Built a new algorithm that is not limited by the availability of multiple similar events.
-> Sudden increases, or “spikes,” (from generated plots) in the volume of tweets in the stream suggest that something important just happened because many people found the need to comment on it.
-> Computes a threshold for the entire event from basic statistics of the set of all slopes for that event from the plot. After trying several formulas , “3*median” as threshold is closely matched to the spikes.
-> After identifying all slopes that exceed the threshold, we generate a list of “spikes” ( <start time> , <peak time> , <end time>) that correspond to the important moments in the events.
-> Extraction of relevant tweets from a set of tweets is done by associating with each tweet a vector of the TF-log(IDF) . We select those tweets which are closest to all other tweets from the event.
-> Find the N sentences contained in our set of tweets that best summarize the set. Our approach is to construct a phrase graph from the longest sentence in each status (tweet) , weight the graph according to frequency of words and a few other heuristics, and then to score the longest sentence using the phrase graph.
-> Created a user interface for the offline model which displays various football matches . 
-> Summary is obtained by selecting the desired match.


Links:

Presentation :  https://docs.google.com/presentation/d/1we-7kp6slHox6EVjyMOKUY-35pwWpRzDO1xFc_OMvRc/edit?usp=sharing


