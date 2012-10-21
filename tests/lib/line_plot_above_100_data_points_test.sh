#!/usr/bin/env bash

actual=./graph-5f23cb7529be3599b0d200bdf85af5b33040c7e5.png

test -e $actual && rm $actual

ruby -e 'x=1; 101.times {puts (x *= 1.02).to_s + " lorem ipsum"}' | \
    bin/sparkler > /dev/null && \
    diff tests/plots/more_than_100_data_points.png $actual
