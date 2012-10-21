sparkler
========

A cli tool directly inspired by [spark][spark]. sparkler produces
graphical plots from whitespace-delimited lists of numbers passed by
other command line arguments.

sparkler makes an attempt to be smart about displaying data in a way
that makes sense while reducing visual noise.

 * if the x-axis has labels, perform sampling for large data sets (so
   that the labels never overlap)
 * fit the graph to the drawing area, so that the graph always fills
   the entire area available for display
 * use log scale if the range of values is large

The output image is written to a file called `graph-<HASH>.png` in the
current working directory, where `<HASH>` is the sha1 hash of the
argument list that was passed to sparkler. This means that each data
set you pass to sparkler should result in a consistent file name that
is unique to that data set. The name of the generated png file is
echoed back to the command line so that you can easily reference it in
your scripts. Eg:

    open `sparkler 0 1 1 2 3 5`

sparkler graphs should fit exactly on a sheet of legal paper when
printed.

## Usage

Just pipe a newline-delimited list of integers to **bin/sparkler** and it
will produce a graphical plot.

The following command will produce a file called `./my_graph.png` that
shows the first nine integers of the Fibonacci Sequence.

    echo 0 1 1 2 3 5 8 13 21 | bin/sparkler

or

    echo "0
    1
    1
    2" | bin/sparkler

Any text after the integer tokens is used as labels for the x-axis:

    echo "0 this is a label
    1 this is another label
    1 and so on
    2 yep labels" | bin/sparkler

You can also pass arguments directly:

    bin/sparkler 0 1 1 2 3 5 8 13 21

or

    bin/sparkler "0
    1
    1
    2"

and also

    bin/sparkler "0 this is a label
    1 this is another label
    1 and so on
    2 fun with labels"

## Installation

The following command will install all dependencies, and should work
on any system with a relatively modern version of Python:

    sudo easy_install numpy matplotlib

You can optionally move or symlink **bin/sparkler** to
**/usr/bin/sparkler** (or anywhere in your path) and it should then be
usable from anywhere on your system, just like any other shell
command.

## How to run the tests

    tests/run

If the exit code is `0`, all is well.

### How do the tests work?

The tests generate graphs off of various inputs and then diff the each
generated image against a fixture image, to validate that the expected
graphs were produced.

## What's not included

**sparkler** is intended to be like **spark:** a dead simple tool that
does the right thing 99% of the time. Thus there are no configuration
options.

The general use case for **sparkler** is: "I am looking at the output
from a shell command and I wonder what it looks like as a graph." More
complex use cases are intentionally not considered.

When you require that level of detail in your analysis, you should
switch to using matplotlib directly, or use another data visualization
tool like R, GNUPlot, Flot or d3.

Specifically, you cannot label the axis nor add a title to the graph
using **sparkler.** For that you can edit the PNG output files using
an image-annotating tool like Photoshop, Skitch or Jing.

And you also cannot combine multiple data series on a single
graph. When you reach a point where you have multiple data series
saved in different files, you should consider using a tool more
powerful than **sparkler.**

[spark]: https://github.com/holman/spark 'spark is an awesome command-line tool for drawing sparklines in your shell'
