# Python in 100 Pages - v2
# argv/csv Exercise

import csv
import sys

filename = sys.argv[1]

with open(filename, 'r') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_data:
        print(row)


