#!/usr/bin/env bash

actual=./graph-eda93b565715058fdfce1ccbfdc9c5018cb7066f.png

test -e $actual && rm $actual

set -x

echo "3
5
8" | bin/sparkler && \
    diff tests/plots/values_newline_delimited.png $actual

