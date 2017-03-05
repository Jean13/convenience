#!/usr/bin/python

# Converts to hex, ascii, decimal, or little-endian.
# Jean Gonzalez, 12/01/2016

import sys


def toHex(string):
	in_hex = string.encode('hex')
	return in_hex


def toLittleEndian(string):
	little_endian = '0x' + "".join(reversed([string[i:i+2] 
		for i in range(0, len(string), 2)]))
	return little_endian


def toDecimal(string):
	in_dec = int(string, 16)
	return in_dec


def toAscii(string):
	in_ascii = string.decode('hex')
	return in_ascii


def main():
	if len(sys.argv[1:]) != 2:
		print "format_convert: Convert to hex, ascii, decimal, or little-endian."
		print "\nUsage: ./format_convert.py <string> <-2hex/-2ascii/-2dec/-2le>"
		print "Example: ./format_convert.py 41 -2ascii\n"
		sys.exit(0)

	# Original input
	to_convert = sys.argv[1]
	mode = sys.argv[2]

	# Conversion
	if mode == '-2hex':
		in_hex = toHex(to_convert)
		little_endian = toLittleEndian(in_hex)
		print 'Original:', to_convert, '\nHex:', '0x' + in_hex
		print 'Little-endian:', little_endian

	elif mode == '-2ascii':
		in_ascii = toAscii(to_convert)
		print 'Original:', to_convert, '\nAscii:', in_ascii

	elif mode == '-2dec':
		in_dec = toDecimal(to_convert)
		print 'Original:', to_convert, '\nDecimal:', in_dec

	elif mode == '-2le':
		inpt = toAscii(to_convert)
		in_hex = toHex(inpt)
		in_LE = toLittleEndian(in_hex)
		print 'Original:', '0x' + to_convert, '\nLittle-endian:', in_LE

	else:
		print 'Improper format. Review and re-submit.\n'
		sys.exit(0)


main()
	
