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
	
	trip_coordinates_zip = data_utils.get_trip_coordinates_zip(trip_data, station_data)
	trip_coordinates_home_coordinates = data_utils.get_trip_coordinates_home_coordinates(trip_coordinates_zip, zip_data)

	#trip_coordinates_home_coordinates = filter(lambda x: data_utils.is_bay_area_resident(x[2]), trip_coordinates_home_coordinates)

	home_coordinates = np.array(zip(*trip_coordinates_home_coordinates)[2])


	start_coordinates = np.array(zip(*trip_coordinates_home_coordinates)[0])

	end_coordinates = np.array(zip(*trip_coordinates_home_coordinates)[1])


	#diff = home_coordinates - start_coordinates

	diff = end_coordinates - start_coordinates

	plt.scatter(diff[:,[1]], diff[:,[0]])


	plt.show()

if __name__ == "__main__":
	main()
