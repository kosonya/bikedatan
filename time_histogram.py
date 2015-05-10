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

	from_home, to_home = data_utils.split_trips_to_from_home(trip_data, station_data, zip_data, debug = False)


	from_home_trip_times = data_utils.get_trip_times_of_day(from_home)
	n, bins, patches = plt.hist(from_home_trip_times, 50, normed=0, facecolor='blue', alpha=0.5)

	to_home_trip_times = data_utils.get_trip_times_of_day(from_home)
	n, bins, patches = plt.hist(to_home_trip_times, 50, normed=0, facecolor='green', alpha=0.5)

	plt.xlabel("Hour of day")
	plt.ylabel("Number of rides")
	plt.title("Rides every hour of day")
	plt.show()

if __name__ == "__main__":
	main()
