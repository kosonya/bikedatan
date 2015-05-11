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

	home_coordinates = zip(*trip_coordinates_home_coordinates)[2]

	#home_coordinates = filter(data_utils.is_bay_area_resident, home_coordinates)
	
	lat, lon = zip(*home_coordinates)

#	m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
#			llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')	#World
#	m = Basemap(projection='merc',llcrnrlat=25,urcrnrlat=50,\
#			llcrnrlon=-130,urcrnrlon=-70,lat_ts=20,resolution='c')	#USA

#	m = Basemap(projection='merc',llcrnrlat=35.5,urcrnrlat=39.9,\
#			llcrnrlon=-124.5,urcrnrlon=-118.5,lat_ts=20,resolution='c')	#Norcal

	m = Basemap(projection='merc',llcrnrlat=37.304294,urcrnrlat=37.840926,\
			llcrnrlon=-122.559453,urcrnrlon=-121.859292,lat_ts=20,resolution='c')	#Bay Area

	m.shadedrelief()
	#m.drawlsmask()

	#m.drawcoastlines()
	m.drawcountries()
	m.drawstates()


	#m.fillcontinents(color='0.8')
	# draw parallels and meridians.
	#m.drawparallels(np.arange(-90.,91.,30.))
	#m.drawmeridians(np.arange(-180.,181.,60.))
	#m.drawmapboundary(fill_color='aqua')
	xs,ys = m(lon,lat)

	m.plot(xs, ys, latlon=False, linestyle='circle marker', marker='o', markerfacecolor='blue', markersize=5)

	#start_coordinates = zip(*trip_coordinates_home_coordinates)[0]
	#lat, lon = zip(*start_coordinates)
	#xs,ys = m(lon,lat)
	#m.plot(xs, ys, latlon=False, linestyle='circle marker', marker='o', markerfacecolor='green', markersize=5)

	#end_coordinates = zip(*trip_coordinates_home_coordinates)[1]
	#lat, lon = zip(*end_coordinates)
	#xs,ys = m(lon,lat)
	#m.plot(xs, ys, latlon=False, linestyle='circle marker', marker='o', markerfacecolor='red', markersize=5)

	plt.show()

if __name__ == "__main__":
	main()
