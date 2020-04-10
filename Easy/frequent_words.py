"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Bonus points (not really, but just for fun):

    Avoid creating an array whose memory footprint is roughly as big as the input text.
    Avoid sorting the entire array of unique words.

"""
def top_three_words(text):
	exceptions = [",", ".", "!", "?", "\"", "#", "$", "&", "*", "@", "~", ";", ":", "\n", "\'"]
	for item in exceptions:
		text = text.replace(item, "")

	text = text.split(" ")

	counter = {}

	for word in text:
		if word in counter:
			counter[word] += 1
		else:
			counter[word] = 1

	sorted_counter = reversed(sorted(counter.items(), key =lambda x: x[1]))

	top_vals = [item for item in sorted_counter]

	print(top_vals)


exceptions = [",", ".", "!", "?", "\"", "#", "$", "&", "*", "@", "~", ";", ":", "\n", "\'"]


with open("walrus.txt") as f:
	for line in f.readlines():
		for item in exceptions:
			line = line.replace(item, "").strip()
		top_three_words(line)