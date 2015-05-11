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
import dateutil.parser
import datetime


def lat_lon_vect_to_km_vect(p1, p2):
	lat1, lon1 = p1
	lat2, lon2 = p2
	p3 = lat2, lon1
	dlat = haversine_dist(p1, p3)
	dlon = haversine_dist(p2, p3)
	if lat2 < lat1:
		dlat = -dlat
	if lon2 < lon1:
		dlon = -dlon
	return dlat, dlon	

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

def load_rebalancing_data():
	fname = "data/02/201402_rebalancing_data.csv"
	lst = load_csv_data(fname)
	res = [(val[0], int(val[1]), int(val[2]), dateutil.parser.parse(val[3])) for val in lst]
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

def get_ride_time_of_day(vals):
	time_string = vals[2]
	time_of_trip = dateutil.parser.parse(time_string)
	start_of_day = datetime.datetime.combine(time_of_trip, datetime.time(0))
	delta = time_of_trip - start_of_day
	hours = float(delta.total_seconds())/3600.0 #Need this to get real-valued hours	
	return hours	
	
def get_trip_times_of_day(trip_data, debug = False):
	res = []
	for vals in trip_data:
		try:
			hours = get_ride_time_of_day(vals)
			res.append(hours)
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

def home_closer_to_start(vals, zip_data, station_data): #Unsafe, might throw an exception
	start_terminal, end_terminal, zip_code = vals[-7], vals[-4], vals[-1]
	start_lat_lon = get_station_lat_lon(station_data, start_terminal)
	end_lat_lon = get_station_lat_lon(station_data, end_terminal)
	home_lat_lon = zip_data[zip_code]
	start_home_dist = haversine_dist(start_lat_lon, home_lat_lon)
	end_home_dist = haversine_dist(end_lat_lon, home_lat_lon)
	return start_home_dist < end_home_dist

def split_trips_to_from_home(trip_data, station_data, zip_data, debug = False):
	from_home = []
	to_home = []
	for vals in trip_data:
		try:
			if vals[-2] != "Subscriber":
				continue
			if home_closer_to_start(vals, zip_data, station_data):
				from_home.append(vals)
			else:
				to_home.append(vals)
		except Exception as e:
			if debug:
				print e
				traceback.print_exc()
	return from_home, to_home


def is_bay_area_resident(coord):
	max_lat, min_lon = 39.833016, -124.499227 #North-West
	min_lat, max_lon = 35.549221, -118.566610 #South-East

	lat, lon = coord

	return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def main():
	pass

if __name__ == "__main__":
	main()
