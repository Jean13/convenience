#!/usr/bin/python

# Converts to hex, ascii, decimal, or little-endian.

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


def toOctal(string):
	in_oct = ""
	c = 0
	for char in string:
		c = ord(char)
		octa = oct(c)
		in_oct += ' ' + str(octa)
	return in_oct


def hexToBin(string):
	in_hex = int(string, 16)
	in_bin = bin(in_hex)[2:]
	return in_bin


def binToHex(string):
	in_hex = hex(int(string, 2))
	return in_hex


def main():
	if len(sys.argv[1:]) != 2:
		print '''
format_convert: Convert to hex, ascii, decimal, octal, binary, or little-endian.
Usage: ./format_convert.py <string> <option>
Example: ./format_convert.py 41 -2ascii

Options:
-2hex		: Ascii to hex
-2ascii		: Hex to ascii
-2dec		: To decimal
-2oct		: To octal
-2le		: Big endian to little endian
-hex2bin	: Hex to binary
-bin2hex	: Binary to hex
		'''
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

	elif mode == '-2oct':
		in_oct = toOctal(to_convert)
		print 'Original:', to_convert, '\nOctal:', in_oct, '\n\n[!] Note: Remove any extra leading zeroes.'

	elif mode == '-2le':
		inpt = toAscii(to_convert)
		in_hex = toHex(inpt)
		in_LE = toLittleEndian(in_hex)
		print 'Original:', '0x' + to_convert, '\nLittle-endian:', in_LE

	elif mode == '-hex2bin':
		in_bin = hexToBin(to_convert)
		print 'Originial:', to_convert, '\nBinary:', in_bin

	elif mode == '-bin2hex':
		in_hex = binToHex(to_convert)
		print in_hex

	else:
		print 'Improper format. Review and re-submit.\n'
		sys.exit(0)


main()
