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
#            awk '{print $1" "$2" "$3}' | uniq -c | tac | \
#            awk '{print $1}' | \
#            xargs python ~/git/Arcane/snippets/python/graphs.py
#
# Or if you want labels on the y axis you can do:
# 
#     git log --since 'september' --format='%ad' --date-order | \
#            awk '{print $1" "$2" "$3}' | uniq -c | tac | \
#            xargs -0 python ~/git/Arcane/snippets/python/graphs.py
#
# There are three use cases in all:
#     1. space-delimited list of values
#     2. newline-delimited list of values
#     3. newline delimited list where each line is a value followed by label text

import matplotlib.pyplot as plt
import sys

if len(sys.argv) == 2 and sys.argv[1].match('\n'):
    raw_values = sys.argv[1].strip().split('\n')

    values = []
    labels = []

    for s in raw_values:
        tokens = s.split()
        cons = tokens.pop(0)
        cdr = ' '.join(tokens)
        values.append(float(cons))
        labels.append(cdr)
        plt.plot(values)
        plt.xticks(range(len(values)), labels, size='small', rotation='vertical')

elif len(sys.argv) == 2:
    raw_values = sys.argv[1].split('\n')
    values = [float(s) for s in raw_values]
    plt.plot(values)

else:
    sys.argv.pop(0)
    raw_values = sys.argv
    values = [float(s) for s in raw_values]
    plt.plot(values)

plt.show()
