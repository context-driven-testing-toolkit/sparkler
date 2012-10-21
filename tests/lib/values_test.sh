#!/usr/bin/env bash

# The sha1 hash in the name of the file is constructed from the
# argument list. So the same argument list should always produce the
# same file name.

actual=./graph-e7001334d9d19559a8bb0dd6015f16e31d15566c.png

test -e $actual && rm $actual

set -x

echo 0 1 1 | bin/sparkler && \
    diff tests/plots/values.png $actual
