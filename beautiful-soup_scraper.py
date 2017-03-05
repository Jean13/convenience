# Web scraping/document downloading template using Beautiful Soup.
# TO-SELF: Edit this further to download the PoC or GTFO publications.
# That PoC version will be my final template version.

import requests, os, bs4

# The starting URL
url = 'http://xkcd.com'
# Store documents in the 'xkcd' folder that we're creating
os.makedirs('xkcd', exist_ok=True)
# This is specific to this example, in this example, the last document has the # sign at the end of the URL - the goal is to stop downloading at the last document
while not url.endswith('#'):
	# Download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	# Find the URL of the comic image - modify tag accordingly
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')

	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			# Download the image
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			# Skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue

	# Save the image to our folder
	imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
	# Necessary loop to save files downloaded using Requests
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	# Get the Prev button's URL
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

