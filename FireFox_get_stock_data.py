from selenium import webdriver
# Module for keyboard keys that are impossible to type into a string value
from selenium.webdriver.common.keys import Keys

# Get data from Seeking Alpha, Guru Focus, and FINRA for a given stock.
# Also get the CNN Fear & Greed Index.

# Works for FireFox in Linux


stock = raw_input("What stock would you like to search for? (Please enter Ticker Symbol in CAPS):\n")

# Set the browser to control
browser = webdriver.Firefox()


# CNN Fear & Greed Index
browser.get('http://money.cnn.com/data/fear-and-greed/')


# Open a new tab
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

# Seeking Alpha
browser.switch_to_window(browser.window_handles[1])
browser.get('https://seekingalpha.com/symbol/{}'.format(stock))


# Open a new tab
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

# GuruFocus
browser.switch_to_window(browser.window_handles[2])
browser.get('https://gurufocus.com/stock/{}'.format(stock))


# Open a new tab
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

# FINRA Market Data
browser.switch_to_window(browser.window_handles[3])
browser.get('http://finra-markets.morningstar.com/MarketData/Default.jsp')

# FINRA search box
f_search = browser.find_element_by_id('ms-finra-autocomplete-box')
f_search.send_keys(stock)
f_search.send_keys(Keys.RETURN)


# Return to main tab
browser.switch_to_window(browser.window_handles[0])

