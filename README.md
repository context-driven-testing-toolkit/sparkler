sparkler
========

A cli tool like spark, that produces graphical plots from
whitespace-delimited lists of numbers passed by other command line
arguments.

The output image is written to a file called `my_graph.png` in the
current working directory. **Older output files will be silently
overwritten.**

## Usage

Just pipe a newline-delimited list of integers to **bin/sparkler** and it
will produce a graphical plot.

You can move or symlink **bin/sparkler** to **/usr/bin/sparkler** (or
anywhere in your path) and it should work.

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

## How to run the tests

    tests/run

If the exit code is `0`, all is well.

### How do the tests work?

The tests generate graphs off of various inputs and then diff the each
generated image against a fixture image, to validate that the expected
graphs were produced.
