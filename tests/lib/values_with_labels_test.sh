#!/usr/bin/env bash

set -x

actual=./graph-3f1c78fb398dba2115de388aaceaedb37f1019a7.png

test -e $actual && rm $actual

set -x

echo "13 foo bar
21 baz boz
34 homer marge" | bin/sparkler && \
    diff tests/plots/values_with_labels.png $actual

