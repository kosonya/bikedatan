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
	empty_times, full_times = data_utils.load_empty_full_station_times_of_day(debug = True)
	n, bins, patches = plt.hist(empty_times, 50, normed=0, facecolor='blue', alpha=0.5)
	n, bins, patches = plt.hist(full_times, 50, normed=0, facecolor='green', alpha=0.5)
	plt.xlabel("Hour of the day")
	plt.ylabel("Observations")
	plt.title("Observations when stations are empty (blue) of full (green)")
	plt.show()


if __name__ == "__main__":
	main()
