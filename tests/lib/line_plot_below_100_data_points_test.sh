#!/usr/bin/env bash

actual=./graph-3dafba200d5ce30cc8b6f1c7fe6a87ebba8626f1.png

test -e $actual && rm $actual



ruby -e 'x=1; 100.times {puts (x *= 1.02).to_s + " lorem ipsum"}' | \
    bin/sparkler > /dev/null && \
    diff tests/plots/line_plot_below_100_data_points.png $actual
