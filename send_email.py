#!/usr/bin/python

'''
Automates the sending of e-mail.

Note: If error with Gmail, it is due to 'access for less secure apps', which might be disabled and needs to be enabled.
See: https://support.google.com/accounts/answer/185833?hl=en/
'''

import smtplib
import sys
from getpass import getpass


try: 
	domain = input("Select the number of your e-mail provider:\n \
		1) Gmail\n \
		2) Yahoo\n \
		3) Outlook/Hotmail\n \
		Selection: ")

	if domain == 1:
		domain = "smtp.gmail.com" 

	elif domain == 2:
		domain = "smtp.mail.yahoo.com"

	elif domain == 3:
		domain = "smtp-mail.outlook.com"

	else:
		print "Please select your e-mail provider by typing a number."

	# Connects to domain over port 587 (SMTP over TLS)
	# For SSL, change to port 465
	smtpObj = smtplib.SMTP(domain, 587)

	# Establish a connection to the SMTP server
	smtpObj.ehlo()

	print "\n[*]Connected to the SMTP server..."

except Exception as e:
	print e
	sys.exit(0)
	
try:
	# Enable TLS encryption. Not necessary if using SSL
	smtpObj.starttls()
	print "[*] TLS encryption successful..."

except Exception as e:
	print e
	sys.exit(0)

my_email = raw_input("Your e-mail address: ")
my_pass = getpass(prompt='Password: ', stream=None)
to_email = raw_input("To: ")

try:
	smtpObj.login(my_email, my_pass)

	print "[*] Login successful..."

except Exception as e:
	print e
	sys.exit(0)

subject = raw_input("Subject: ")
message = raw_input("Message: ")

try:

	# <'sender'>, <'recipient'>, <'Subject: <subject> \n <body>'>
	# The \n starts the body of the e-mail
	smtpObj.sendmail(my_email, to_email,
	'Subject:' + subject + '\n' + message)

	print "[*] Successfully sent message."


except Exception as e:
	print e
	sys.exit(0)

smtpObj.quit()

