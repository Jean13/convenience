#!/usr/bin/python

'''
Finds phone numbers and email addresses in the clipboard.
Suggested usage:  
	Press CTRL-A to select all the text, 
	Press CTRL-C to copy it to the clipboard, 
	Run find_phone_email.py

'''


import pyperclip
import re


phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# area code
	(\s|-|\.)?			# separator
	(\d{3})				# first 3 digits
	(\s|-|\.)			# separator
	(\d{4})				# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)''', re.VERBOSE)


emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+		# username
	@				# @ symbol
	[a-zA-Z0-9.-]+			# domain name
	(\.[a-zA-Z]{2,4})		# dot-something
	)''', re.VERBOSE)


# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
	# Area code, first three digits, last four digits, and extension
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
	# Join since pyperclip.copy() takes only a single string, not a list of strings
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))

else:
	print('No phone numbers or email addresses found.')


