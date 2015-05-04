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

def load_csv_data(fname):

	with open(fname, "r") as f: #closes the file automatically
		res = []
		next(f)
		for line in f:
			line.rstrip('\n') #delete last \n only if present
			vals = line.split(',')
			res.append(vals)
		return res

def load_trip_data():
	fname = "data/02/201402_trip_data.csv"
	res = load_csv_data(fname)
	return res


def load_station_data():
	fname = "data/02/201402_station_data.csv"
	res = load_csv_data(fname)
	return res



def main():
	pass

if __name__ == "__main__":
	main()
