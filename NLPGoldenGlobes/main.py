import parser
import result

def main_function(awardFile, tweetsFile):
	allResults = []
	list_tweets = parse_tweets(tweetsFile)
	list_awards = parse_awards(awardFile)

	for award in list_awards:
		winner = get_Winner(award,list_tweets) #winner will resurn 
		new_result = Result(award.unparsed,winner)
		new_result.prettyprint()
		allResults.append(new_result)
	return allResults

def get_Winner(award, list_tweets): 
	pass