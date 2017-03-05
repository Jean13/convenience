# Searches through the SkyScanner API for flight data.

'''
For how to get an API key: https://github.com/Skyscanner/skyscanner-python-sdk
For SDK Usage: https://skyscanner.readthedocs.io/en/latest/usage.html
For official Flight API: http://business.skyscanner.net/portal/en-GB/Documentation/FlightsLivePricingList
For Schemas: http://business.skyscanner.net/portal/en-GB/Documentation/CodeSchemas
For IATA Codes: http://www.iata.org/publications/Pages/code-search.aspx
'''

from skyscanner.skyscanner import Flights, FlightsCache
import sys
import json

API_KEY = ""

flights_service = Flights(API_KEY)
flights_cache_service = FlightsCache(API_KEY)


# Convert the data to JSON format for more organized view
def make_json(data):
	in_json = json.dumps(data, indent=1)
	return in_json


# Get cheapest price by date
def price_by_date():
	user_market = raw_input("Please enter your home country (E.g., US): ")
	user_currency = raw_input("Please enter your desired currency (E.g., USD): ")
	user_locale = 'en-US'
	user_origin = raw_input("City that you are flying from (E.g., NYC): ")
	user_destination = raw_input("City that you are flying to (E.g., PAR): ")

	way = raw_input("Is this a one-way or a round-way trip? Type 'O' or 'R': ")
	if way == 'O':
		user_outbound = raw_input("Departing date (yyyy-mm-dd): ")
		user_inbound = ''

	elif way == 'R':
		user_outbound = raw_input("Departing date (yyyy-mm-dd): ")
		user_inbound = raw_input("Returning date (yyyy-mm-dd): ")

	user_adults = int(raw_input("Number of adults: "))
	user_children = int(raw_input("Number of children: "))
	user_infants = int(raw_input("Number of infants: "))

	result = flights_cache_service.get_cheapest_price_by_date(
	    market=user_market,
	    currency=user_currency,
	    locale=user_locale,
	    originplace=user_origin,
	    destinationplace=user_destination,
	    outbounddate=user_outbound,
	    inbounddate=user_inbound,
	    adults=user_adults,
	    children=user_children,
	    infants=user_infants).parsed

	return make_json(result)
	

# Get cheapest price by route
def price_by_route():
	user_market = raw_input("Please enter your home country (E.g., US): ")
	user_currency = raw_input("Please enter your desired currency (E.g., USD): ")
	user_locale = 'en-US'
	user_origin = raw_input("City that you are flying from (E.g., NYC): ")
	user_destination = raw_input("City that you are flying to (E.g., PAR): ")

	way = raw_input("Is this a one-way or a round-way trip? Type 'O' or 'R': ")
	if way == 'O':
		user_outbound = raw_input("Departing date (yyyy-mm-dd): ")
		user_inbound = ''

	elif way == 'R':
		user_outbound = raw_input("Departing date (yyyy-mm-dd): ")
		user_inbound = raw_input("Returning date (yyyy-mm-dd): ")

	user_adults = int(raw_input("Number of adults: "))
	user_children = int(raw_input("Number of children: "))
	user_infants = int(raw_input("Number of infants: "))

	result = flights_cache_service.get_cheapest_price_by_route(
	    market=user_market,
	    currency=user_currency,
	    locale=user_locale,
	    originplace=user_origin,
	    destinationplace=user_destination,
	    outbounddate=user_outbound,
	    inbounddate=user_inbound,
	    adults=user_adults,
	    children=user_children,
	    infants=user_infants).parsed

	return make_json(result)


def main():

	method = ''

	while method != 'a' or method != 'b':

		print "\nWelcome to the SkyScanner program."
		print "Please select 'a' or 'b' for your preferred method of flight " \
			"search:"
		print "\ta -  Cheapest price by date"
		print "\tb -  Cheapest price by route"
		print "\tc -  Quit\n"

		method = raw_input("Method: ")

		if method == 'a':
			print price_by_date()

		elif method == 'b':
			print price_by_route()

		elif method == 'c':
			print "Thank you for using Sky Scanner. Goodbye!\n"
			sys.exit(0)

		else:
			print "[!] Please type 'a' or 'b' (without the quotes).\n"

main()

