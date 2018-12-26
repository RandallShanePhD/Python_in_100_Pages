# Python in 100 Pages - v2
# argv Example

import sys

friends = sys.argv[1:]
for friend in friends:
    print('Hello there %s!' % friend)

