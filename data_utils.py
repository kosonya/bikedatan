#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import traceback
import math

def haversine_dist(p1, p2):
	#print p1
	#print p2
	lat1, lon1 = map(math.radians, p1)
	lat2, lon2 = map(math.radians, p2)
	earth_radius = 6367.0
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = math.pow(math.sin(dlon/2.0), 2) + math.cos(lon1) * math.cos(lon2) * math.pow(math.sin(dlat/2.0), 2)
	c = 2.0 * math.asin(math.sqrt(a))
	km = earth_radius * c
	return km

def load_csv_data(fname):

	with open(fname, "r") as f: #closes the file automatically
		res = []
		next(f)
		for line in f:
			line = line.rstrip('\n') #delete last \n only if present
			line = line.rstrip('\r') #delete last \r only if present
			vals = line.split(',')
			res.append(vals)
		return res

def load_trip_data():
	fname = "data/02/201402_trip_data.csv"
	res = load_csv_data(fname)
	return res


def load_station_data():
	fname = "data/02/201402_station_data.csv"
	lst = load_csv_data(fname)
	res = {vals[0]: vals[1:] for vals in lst}
	return res

def get_station_lat_lon(station_data, station_id):
	vals = station_data[station_id]
	lat, lon = float(vals[1]), float(vals[2])
	return lat, lon

def load_zip_data(debug = False):
	fname = "data/zip_codes_states.csv"
	with open(fname, "r") as f: #closes the file automatically
		res = {}
		next(f)
		for line in f:
			try:
				line = line.rstrip('\n').replace('"', '')
				vals = line.split(',')
				zip_code = vals[0]
				lat, lon = float(vals[1]), float(vals[2])
				res[zip_code] = lat, lon
			except Exception as e:
				if debug:
					print e
					traceback.print_exc()
		return res

def get_trip_coordinates_zip(trip_data, station_data, debug = False):
	res = []
	for vals in trip_data:
		try:
			if vals[-2] != "Subscriber":
				continue
			start_terminal, end_terminal, zip_code = vals[-7], vals[-4], vals[-1]
			start_lat_lon = get_station_lat_lon(station_data, start_terminal)
			end_lat_lon = get_station_lat_lon(station_data, end_terminal)
			res.append( (start_lat_lon, end_lat_lon, zip_code) )
		except Exception as e:
			if debug:
				print e
				traceback.print_exc()
	return res
		
def get_trip_coordinates_home_coordinates(trip_coordinates_zip, zip_data, debug = False):
	res = []
	for vals in trip_coordinates_zip:
		try:
			start_lat_lon, end_lat_lon, zip_code = vals
			zip_lat_lon = zip_data[zip_code]
			res.append( (start_lat_lon, end_lat_lon, zip_lat_lon) )
		except Exception as e:
			if debug:
				print e
				traceback.print_exc()
	return res

def is_bay_area_resident(coord):
	max_lat, min_lon = 39.833016, -124.499227 #North-West
	min_lat, max_lon = 35.549221, -118.566610 #South-East

	lat, lon = coord

	return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def main():
	pass

if __name__ == "__main__":
	main()
