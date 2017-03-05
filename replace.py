#!/usr/bin/python

def replace():

	f = raw_input("Enter the path to the file you want to modify:\n")

	with open(f, 'r') as file:
			fp = file.read()

	search = raw_input("Enter the text you want to replace:\n")

	new = raw_input("Enter the text you want to replace with:\n")

	data = fp.replace(search, new)

	with open(f, 'w') as file:
		file.write(data)

replace()

