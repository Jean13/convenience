#!/usr/bin/python

import sys
from subprocess import call

# Search the web through Google, Baidu or Yandex.
# Why did I write this? Because it's faster than opening a web page


def google(data):
	basic = "https://www.google.com/search?q="
	search = basic + data
	return call(["x-www-browser", search])


def baidu(data):
	basic = "http://www.baidu.com/s?wd="
	search = basic + data
	return call(["x-www-browser", search])


def yandex(data):
	basic = "https://www.yandex.com/search/?text="
	search = basic + data
	return call(["x-www-browser", search])


def main():
	
	if len(sys.argv[1:]) != 2:
		print "international_search.py: Search for data using Google, " \
			"Baidu or Yandex straight from the terminal."
		print "\nUsage: python international_search.py <query> <-G \ -B \ -Y>"
		sys.exit(0)
	
	try:
		data = sys.argv[1]

		engine = sys.argv[2]

		if engine == "-G" or engine == "-g":
			google(data)
		elif engine == "-B" or engine == "-b":
			baidu(data)
		elif engine == "-Y" or engine == "-y":
			yandex(data)
		else:
			print "[!] Please follow the appropriate format..."

	except Exception as e:
		print e
		sys.exit(0)

main()

