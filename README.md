sparkler
========

A cli tool like spark, that produces graphical plots from
whitespace-delimited lists of numbers passed by other command line
arguments.

The output image is written to a file called `my_graph.png` in the
current working directory. **Older output files will be silently
overwritten.**

## How to run the tests

    tests/run

If the exit code is `0`, all is well.

### How do the tests work?

The tests generate graphs off of trivial inputs and then inpsect the
checksum of each generated image to validate that the expected graphs
were produced.
