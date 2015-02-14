import re

memoized = {}
def construct_abbrev(num_letters, word):

	if (num_letters,word) in memoized:
		print "returning cached " + str((num_letters, word)) + " :" + str(memoized[(num_letters, word)])
		return memoized[(num_letters,word)]
	# TODO:
	results = []

	if num_letters == 0:
		results.append(str(len(word)))
		return results
	
	if num_letters >= len(word):
		results.append(word)
		return results

	# include the letter
	abbrevs = construct_abbrev(num_letters - 1, word[1:])

	for s in abbrevs:
		results.append(word[0] + s)

	abbrevs = construct_abbrev(num_letters, word[1:])

	for s in abbrevs: 
		title_search = re.search('^(\d+)(\w+)', s, re.IGNORECASE)
		if title_search:
			results.append(str(int(title_search.group(1)) + 1) + title_search.group(2))
		else:
			results.append('1' + s)
	memoized[(num_letters,word)] = results
	return results

#print construct_abbrev(0, 'car')
print construct_abbrev(2, 'apple')
# print construct_abbrev(2, 'car')


def find_shortest_unique(num_letter, words, words_remaining):
	if len(words_remaining) == 0:
		return []
	new_words = words_remaining[:]
	unique_abbrev = {}
	for word in words:
		for abbrev in construct_abbrev(num_letter, word):
			#found unique abbrev
			if abbrev not in unique_abbrev:
				unique_abbrev[abbrev] = []

			unique_abbrev[abbrev].append(word)
	x = [(key, value[0]) for key, value in unique_abbrev.items() if len(value) ==1]
	result = []
	for key, word in x:
		if word in new_words:
			new_words.remove(word)
			result.append(key)
	#print num_letter, x, unique_abbrev, new_words

	return result + find_shortest_unique(num_letter+1, words,  new_words)
	# use collision map to determine if the abbrev is unique
	

#words = ['bad', 'bar', 'far', 'dad', 'sad']
#print find_shortest_unique(0, words, words)
