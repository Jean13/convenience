# Template for parsing XML files from the Internet

import requests
import bz2
import zipfile
# Module for parsing XML into a DOM document object
from xml.dom import minidom
# Library for plotting
import matplotlib.pyplot as plt
import matplotlib.patches as ptc


# Pattern to save what is being streamed to a file
def download_photo(filename):

	# The URL to get the image from - adjust accordingly
	target = raw_input("Enter the target URL.\nExample: " \
	"https://www.hackthissite.org/missions/prog/4/XML\n: ")

	# Cookies - adjust accordingly
	cookieName1 = raw_input("Enter the cookie name.\nExample: PHPSESSID\n: ")
	cookieValue1 = raw_input("Enter the cookie's value.\nExample: " \
	"240jp2ne8flm88v8c3qm41htf5\n: ")
	cookies = {cookieName1: cookieValue1}

	# Referer - adjust accordingly
	referer = raw_input("Enter the referer.\nExample: " \
	"https://www.hackthissite.org/missions/prog/4/\n: ")

	# Headers - adjust accordingly
	headers = {'Referer': referer}

	# Verifying we can connect
	req = requests.get(target, cookies=cookies)
	if req.status_code != requests.codes.ok:
	    raise ValueError('Poof! Unable to connect to target t(X_X)t')
	else:
	    print('+++ Connected to target. Starting operation...\n')

	r = requests.get(target, cookies=cookies, stream=True)
	 
	with open(filename, 'wb') as fd:
		for chunk in r.iter_content():
			fd.write(chunk)	

		return filename


# Decompress BZ2 format
def decompress_bz2(filepath):

	download_photo(filepath)

	try:
		# Open the BZ2 file
		zipfile = bz2.BZ2File(filepath)
		# Get the decompressed data
		data = zipfile.read()
		# Assuming the filepath ends with .bz2
		newfilepath = filepath[:-4]
		# Write an uncompressed file
		open(newfilepath, 'wb').write(data)

		return newfilepath

	except IOError as e:
		print "[!] Please verifiy you entered the correct cookie value.\n"
		print e


def unzip(filepath):

	download_photo(filepath)

	try:
		with zipfile.ZipFile(filepath, "r") as ext:
			newfilepath = ext.extractall("./")
		return newfilepath

	except IOError as e:
		print "[!] Please verifiy you entered the correct cookie value.\n"
		print e


filepath = raw_input("Enter the filepath.\nExample: plotMe.xml.bz2\n: ")

what = raw_input("Is the current file format ZIP, BZ2 or XML? Choose: Z, B, or X\n: ")
	
if what == 'Z' or 'z' or 'ZIP':
	to_parse = unzip(filepath)

elif what == 'B' or 'b' or 'BZ2': 
	to_parse = decompress_bz2(filepath)

else: 
	newfilepath = filepath


# Parse the XML - adjust accordingly
def parse_xml():
	xmldoc = minidom.parse(to_parse)
	plt.axes()

	lines = xmldoc.getElementsByTagName('Line')
	arcs = xmldoc.getElementsByTagName('Arc')

	for line in lines:
		xstart = line.getElementsByTagName('XStart')[0].firstChild.data
		xend = line.getElementsByTagName('XEnd')[0].firstChild.data

		ystart = line.getElementsByTagName('YStart')[0].firstChild.data
		yend = line.getElementsByTagName('YEnd')[0].firstChild.data

		try:
			color = line.getElementsByTagName('Color')[0].firstChild.data
		except IndexError:
			# If the color is white, set it to black
			color = 'black'

		plt.plot([float(str(xstart)),float(str(xend))],[float(str(ystart)),float(str(yend))],color)

	for arc in arcs:
		x = float(str(arc.getElementsByTagName('XCenter')[0].firstChild.data))
		y = float(str(arc.getElementsByTagName('YCenter')[0].firstChild.data))

		radius = 2 * float(str(arc.getElementsByTagName('Radius')[0].firstChild.data))

		arcstart = float(str(arc.getElementsByTagName('ArcStart')[0].firstChild.data))
		arcend = float(str(arc.getElementsByTagName('ArcExtend')[0].firstChild.data))+arcstart

		try:
			colour = arc.getElementsByTagName('Color')[0].firstChild.data
		except IndexError:
			# If the color is white, set it to black
			colour = 'black'

		arc = ptc.Arc((x,y),radius,radius,0,arcstart,arcend,color=colour)
		plt.gca().add_patch(arc)

	plt.axis('scaled')
	plt.show()
	y1 = 0
	x2 = 0
	y2 = 0
	color = ''
	r = 0

	for element in root.iter("*"):
		if element.tag == 'Line' or element.tag == 'Arc':
			if before == 'Line' and count == 5:
				plot_line(x1, y1, x2, y2, 'black')
			elif before == 'Arc' and count == 6:
				plot_arc(x1, y1, r, x2, y2, 'black')
		if element.tag == 'Line' or element.tag == 'Arc':
			if before == 'Line' and count == 6:
				plot_line(x1, y1, x2, y2, color)
			elif before == 'Arc' and count == 7:
				plot_arc(x1, y1, r, x2, y2, color)
		if element.tag == 'Line' or element.tag == 'Arc':
			before = element.tag
			count = 0

		if before == 'Line':
			if element.tag == 'XStart':
				x1 = float(element.text)
			if element.tag == 'YStart':
				y1 = float(element.text)
			if element.tag == 'XEnd':
				x2 = float(element.text)
			if element.tag == 'YEnd':
				y2 = float(element.text)
			if element.tag == 'Color':
				color = element.text
			count += 1

		if before == 'Arc':
			if element.tag == 'XCenter':
				x1 = float(element.text)
			if element.tag == 'YCenter':
				y1 = float(element.text)
			if element.tag == 'Radius':
				r = float(element.text)
			if element.tag == 'ArcStart':
				x2 = float(element.text)
			if element.tag == 'ArcExtend':
				y2 = float(element.text)
			if element.tag == 'Color':
				color = element.text
			count += 1

	return show()

parse_xml()

