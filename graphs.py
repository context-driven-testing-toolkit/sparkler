#!/usr/bin/env python
"""

A CLI tool like spark, that produces sparklines from
whitespace-delimited lists of numbers passed by other command line
arguments. See https://github.com/holman/spark

There are three valid use cases:

1. space-delimited list of values (no labels, all values on one line):

    git log --since 'september' --format='%ad' --date-order | \
        awk '{print $1" "$2" "$3}' | uniq -c | tac | awk '{print $1}' | \
        xargs python graphs.py

2. newline-delimited list of values (no labels, newline-delimited):

     git log --since 'september' --format='%ad' --date-order | \
         awk '{print $1" "$2" "$3}' | uniq -c | tac | awk '{print $1}' | \
         python graphs.py

3. newline-delimited list where each line is a value followed by label text:

    git log --since 'september' --format='%ad' --date-order | \
        awk '{print $1" "$2" "$3}' | uniq -c | tac | \
        python graphs.py

"""

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_plot(values):
    plt.plot(values, color='#333333', linewidth=2.0)

lines_of_input = sys.stdin.readlines()

if len(sys.argv) == 1 and len(lines_of_input) > 0:
    raw_values = lines_of_input

    values = []
    labels = []

    for s in raw_values:
        tokens = s.split()
        cons = tokens.pop(0)
        cdr = ' '.join(tokens)
        values.append(float(cons))
        labels.append(cdr)
        make_plot(values)
        plt.xticks(range(len(values)), labels, size='small', rotation=75)

elif len(sys.argv) == 2:
    raw_values = sys.argv[1].split('\n')
    values = [float(s) for s in raw_values]
    make_plot(values)

else:
    sys.argv.pop(0)
    raw_values = sys.argv
    values = [float(s) for s in raw_values]
    make_plot(values)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(14, 8.65)
fig.savefig('./my_graph.png', dpi=100, bbox_inches='tight')
