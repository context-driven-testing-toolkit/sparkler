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

raw_values = sys.argv
values = []

for s in raw_values:
    tokens = s.split()
    cons = tokens.pop(0)
    cdr = tokens
    values.append(float(cons))

# values = [float(s) for s in raw_values]

plt.plot(values)
plt.xticks(range(len(values)), ['foo'], size='small', rotation='vertical')
plt.show()
