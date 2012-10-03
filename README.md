sparkler
========

A cli tool like spark, that produces graphical plots from
whitespace-delimited lists of numbers passed by other command line
arguments.

The output image is written to a file called `my_graph.png` in the
current working directory. **Older output files will be silently
overwritten.**

## Usage

Just pipe a newline-delimited list of integers to **sparkler** and it
will produce a graphical plot.

The following command will produce a file called `./my_graph.png` that
shows the first nine integers of the Fibonacci Sequence.

    echo 0 1 1 2 3 5 8 13 21 | python graphs.py

You can also pass arguments directly:

    python graphs.py 0 1 1 2 3 5 8 13 21

## How to run the tests

    tests/run

If the exit code is `0`, all is well.

### How do the tests work?

The tests generate graphs off of trivial inputs and then inpsect the
checksum of each generated image to validate that the expected graphs
were produced.
