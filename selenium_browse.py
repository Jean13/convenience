# Web scraping template for automation of clicking, typing, and more.
# For more info: https://automatetheboringstuff.com/chapter11/

from selenium import webdriver
# Module for keyboard keys that are impossible to type into a string value
from selenium.webdriver.common.keys import Keys

# Set the browser to control
browser = webdriver.Firefox()

# Starting website
browser.get('https://inventwithpython.com')

# Searches for a specific string in a website
linkElem = browser.find_element_by_link_text('Read It Online')
# Clicks/follows the link
linkElem.click()

# Clicks the browser's Back button
browser.back()
browser.refresh

browser.get('https://google.com')
# id of Google search box
google_search = browser.find_element_by_id('lst-ib')
google_search.send_keys('testing')
# name of Google "go" button
google_go = browser.find_element_by_name('btnG')
google_go.click()

# For some reason, Google always freezes any further URL queries
browser.back()
browser.back()

# Filling out and submitting a form - modify accordingly
browser.get('https://mail.yahoo.com')
yahoo_email = browser.find_element_by_id('login-username')
yahoo_email.send_keys('someone@yahoo.com')
yahoo_next = browser.find_element_by_id('login-signin')
yahoo_next.click()
yahoo_pass = browser.find_element_by_id('passwd-field')
yahoo_pass.send_keys('nottherealpassword')
yahoo_pass.submit()



