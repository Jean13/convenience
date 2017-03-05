#!/usr/bin/python

import sys

'''
Finds text in a document given their location in a second file.
Finds text given the following order: (Paragraph no., Sentence no., Word no.)

'''

def searchWordsInDocument():
	if len(sys.argv[1:]) != 2:
		print "document_word_finder.py: Find words in a document given " \
			"their location in a second file."
		print "\nUsage: ./document_word_finder.py <document to search in> " \
			"<document with locations>"
		print "Example: ./document_word_finder.py book.txt search.txt\n"
		sys.exit(0)


	# The document to search in
	data = sys.argv[1]
	with open(data, 'r') as f:
		data = f.read().split('\n\n')

	# The document that has the locations to search for
	search = sys.argv[2]
	with open(search, 'r') as f:
		for line in f:
			to_search = line.split(",")
			paragraph = int(to_search[0])
			sentence = int(to_search[1])
			word = int(to_search[2])


			for p in [(paragraph, sentence, word)]:
				print "\nParameters: {}-{}-{}".format \
				(paragraph, sentence, word)
				print "Resulting text:", \
				data[p[0]-1].split('\n')[p[1]-1].split(' ')[p[2]-1]

searchWordsInDocument()

