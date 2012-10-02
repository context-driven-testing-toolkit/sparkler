#!/usr/bin/env python

# A cli tool like spark, that produces sparklines from
# whitespace-delimited lists of numbers passed by other command line
# arguments.
#
# see http://matplotlib.org/users/pyplot_tutorial.html
#     http://stackoverflow.com/questions/1992640
#
# Currently usage is like:
#
#     git log --since='september' --format='%ad' --date-order | \
#        awk '{print $1" "$2" "$3}' | uniq -c | tac | \
#        awk '{print $1}' | \
#        xargs python ~/git/Arcane/snippets/python/graphs.py

import matplotlib.pyplot as plt
import sys

sys.argv.pop(0)

args = [float(s) for s in sys.argv]

plt.plot(args)
plt.xticks(range(len(sys.argv)), ['foo'], size='small', rotation='vertical')

plt.show()
