sparkler: graphical plots from shell command output
========

## Usage

Just pipe a newline-delimited list of integers to **bin/sparkler** or **bin/spc_chart** and it
will produce a graphical plot.

### Labeled Series, Including Time Series

`spc_chart` and `sparkler` both support labels on data series as long as the first value on each 
line is a number and the rest of the line is the label. If there are many labels sampling will 
be performed so that only a few labels appear on the x-axis. This keeps the graph readable even
if there are hundreds of data points.

For example this can be useful if you have a time series:

    echo "27 Wed Sep 26 13:50:57 EDT 2018
    13 Wed Oct 3 13:50:56 EDT 2018
    9 Wed Sep 19 13:50:51 EDT 2018
    4 Wed Oct 3 13:50:51 EDT 2018
    25 Wed Sep 26 13:50:51 EDT 2018
    10 Wed Oct 17 13:50:49 EDT 2018
    29 Wed Oct 17 13:45:51 EDT 2018
    31 Wed Oct 17 13:45:49 EDT 2018
    34 Wed Oct 17 13:44:52 EDT 2018
    16 Wed Oct 17 13:44:51 EDT 2018
    1 Wed Oct 17 13:43:53 EDT 2018
    17 Wed Oct 17 13:43:51 EDT 2018
    5 Wed Oct 17 13:42:54 EDT 2018
    0 Wed Oct 17 13:42:51 EDT 2018
    9 Wed Oct 17 13:40:55 EDT 2018
    21 Wed Oct 17 13:40:51 EDT 2018
    11 Wed Sep 19 11:50:57 EDT 2018" \
    | bin/spc_chart

This produces a chart file named `spc-chart-d8e9d9e86bcc714332e8954a6bafd2521b86a242.png`

If you open that PNG file you will see this chart:

<img src="https://i.imgur.com/ZW6PdlBl.png" 
   alt="a dot plot with control lines above and below the time series">

### Simple Use

The following command will produce a graphical plot that shows the
first nine integers of the Fibonacci Sequence.

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

## Synopsis

A cli tool directly inspired by [spark][spark]. sparkler produces
graphical plots from whitespace-delimited lists of numbers passed by
other command line arguments.

In 2017 I wrote [an introductory article about sparkler.](http://infiniteundo.com/post/158800222608/sparkler-graphs-in-terminal "it has some nice screenshots")

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
