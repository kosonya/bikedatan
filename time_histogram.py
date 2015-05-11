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

import data_utils

import sys
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np




def main():
	trip_data = data_utils.load_trip_data()
	station_data = data_utils.load_station_data()
	zip_data = data_utils.load_zip_data()


	if True:
		from_home, to_home = data_utils.split_trips_to_from_home(trip_data, station_data, zip_data, debug = False)

		print "len(from_home)", len(from_home), "len(to_home)", len(to_home)

		from_home_trip_times = data_utils.get_trip_times_of_day(from_home)
		n, bins, patches = plt.hist(from_home_trip_times, 50, normed=0, facecolor='blue', alpha=0.5)

		to_home_trip_times = data_utils.get_trip_times_of_day(to_home)
		n, bins, patches = plt.hist(to_home_trip_times, 50, normed=0, facecolor='green', alpha=0.5)

		plt.xlabel("Hour of day")
		plt.ylabel("Number of rides")
		plt.title("Rides from home (blue) and to home (green)")
		plt.show()
	elif False:
		

		trip_data_s = filter(lambda x: x[-2] == "Subscriber", trip_data)
		trip_times_s = data_utils.get_trip_times_of_day(trip_data_s)
		n, bins, patches = plt.hist(trip_times_s, 50, normed=0, facecolor='blue', alpha=1)

		trip_data_ns = filter(lambda x: x[-2] != "Subscriber", trip_data)
		trip_times_ns = data_utils.get_trip_times_of_day(trip_data_ns)
		n, bins, patches = plt.hist(trip_times_ns, 50, normed=0, facecolor='green', alpha=0.75)

		plt.xlabel("Hour of day")
		plt.ylabel("Number of rides")
		plt.title("Rides of subscribers (blue) and non-subscribers (green)")
		plt.show()
	elif False:
		
		trip_data = filter(lambda x: x[-2] == "Subscriber", trip_data)


		has_zip = filter(lambda x: zip_data.has_key(x[-1]), trip_data)

		trip_times = data_utils.get_trip_times_of_day(trip_data)
		n, bins, patches = plt.hist(trip_times, 50, normed=0, facecolor='blue', alpha=1)


		has_zip_times = data_utils.get_trip_times_of_day(has_zip)
		n, bins, patches = plt.hist(has_zip_times, 50, normed=0, facecolor='green', alpha=0.75)

		plt.xlabel("Hour of day")
		plt.ylabel("Number of rides")
		plt.title("Rides of subscribers (blue) and non-subscribers (green)")
		plt.show()


if __name__ == "__main__":
	main()
