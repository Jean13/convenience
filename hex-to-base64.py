#!/usr/bin/python

import sys
from binascii import unhexlify, b2a_base64


def main():
	if len(sys.argv[1:]) != 2:
		print "hex-to-base64: Convert from hex to base64 and vice-versa."
		print "\nUsage: ./hex-to-base64.py <string> <-2base64/-2hex>"
		sys.exit(0)

	# Original input
	to_convert = sys.argv[1]
	mode = sys.argv[2]

	# Conversion
	if mode == '-2base64':
		raw = unhexlify(to_convert)
		ascii = to_convert.decode('hex')
		in_b64 = b2a_base64(raw)
		print '\nOriginal:', to_convert
		print 'Ascii:', ascii
		print 'Base64-encoded:', in_b64

	elif mode == '-2hex':
		in_hex = to_convert.encode('hex')
		little_endian = '0x' + "".join(reversed([in_hex[i:i+2] 
			for i in range(0, len(in_hex), 2)]))
		print '\nOriginal:', to_convert, '\nHex:', '0x' + in_hex
		print 'Little-endian:', little_endian

	else:
		print 'Improper format. Review and re-submit.\n'
		sys.exit(0)


main()
