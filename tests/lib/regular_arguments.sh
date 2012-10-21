#!/usr/bin/env bash

actual=./graph-9ee5a8d183642ce661f2ca182dead4457215ee01.png

test -e $actual && rm $actual

set -x

bin/sparkler 55 89 144 && \
    diff tests/plots/regular_arguments.png $actual
