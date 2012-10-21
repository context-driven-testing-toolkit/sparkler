#!/usr/bin/env bash

actual=./graph-ee3e64910e82f16bcfd238702fe262a15923a514.png

test -e $actual && rm $actual



ruby -e 'x=1; 50.times {puts (x += 1).to_s + " lorem ipsum"}' | \
    bin/sparkler > /dev/null && \
    diff tests/plots/many_labels_50.png $actual
