#!/usr/bin/python

# Runs the radare2 web-ui Enyo.
# r2 -q -e http.ui=enyo -c=H <program name>

import sys
import subprocess

def main():
	if len(sys.argv[1:]) != 1:
		print "Enter the path of the file you want to open in R2 Web-UI"
		print "Usage: ./r2_ui.py <program path>\n"
		sys.exit(0)

	program = sys.argv[1]

	try:
		bash_command = 'r2 -q -e http.ui=enyo -c=H ' + program

		process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()

	except:
		print "\n[*] Program closed.\n"

main()

