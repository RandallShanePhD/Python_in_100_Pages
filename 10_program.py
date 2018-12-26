# Lesson 10
# Input/Output

import csv
import sys

print('There are %i arguments' % len(sys.argv))
print('The arguments are:', sys.argv)

with open(sys.argv[1], 'r') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_data:
        print(row)


# csv writing
import csv
short_data = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

with open('write_data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for row in short_data:
        print(row)
        writer.writerow(row)
