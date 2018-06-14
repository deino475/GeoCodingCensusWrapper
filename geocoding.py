import json
import requests

class GeoCodingObject(object):
	def __init__(self,geoid,lat,lng, tract):
		self.geoid = geoid
		self.lat = lat
		self.lng = lng
		self.tract = tract

def geocoding_api(street, city, state, zip_code):
	base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address?benchmark=Public_AR_Census2010&format=json&vintage=Census2010_Census2010&layers=14"
	street = "&street=" + str(street)
	city = "&city=" + str(city)
	state = "&state" + str(state)
	zip_code = "&zip=" + str(zip_code)
	url = base_url + street + city + state + zip_code
	response = requests.get(url)
	json_response = json.loads(response.text)

	lng = json_response['result']['addressMatches'][0]['coordinates']['x']
	lat = json_response['result']['addressMatches'][0]['coordinates']['y']
	geoid = json_response['result']['addressMatches'][0]['geographies']['Census Blocks'][0]['GEOID']
	tract = json_response['result']['addressMatches'][0]['geographies']['Census Blocks'][0]['TRACT']
	return GeoCodingObject(geoid, lat, lng, tract)
